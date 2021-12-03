from typing import List
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import redis
import uuid
import json

import requests
import os
import shutil
import img2pdf
from natsort import natsorted
from PIL import Image


from scraping import listup_image

REDIS_SERVER_NAME = "redis"

class UrlItem(BaseModel):
    url: str

class GenerateItem(BaseModel):
    uuid: str
    indexes: list

# Fast API Launch
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=origins,
    allow_headers=origins
)

# Redis Connection
redis_connection = redis.Redis(host=REDIS_SERVER_NAME, port=6379, db=0)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/listup")
async def get_listup(url: UrlItem):
    img_list = listup_image(url=url.url)
    str_data = json.dumps(img_list)
    connection_id = str(uuid.uuid4())

    redis_connection.set(connection_id, str_data)

    return {
        "connection_id": connection_id,
        "img_list": str_data
    }

@app.post("/generate")
async def generate(item: GenerateItem):
    str_data = redis_connection.get(item.uuid)
    img_list = json.loads(str_data)

    selected_img_list = list(map(int, item.indexes))

    tmp_dir = os.path.join('tmp', item.uuid)
    os.makedirs(tmp_dir, exist_ok=True)

    i_count = 0
    for idx in selected_img_list:
        content = img_list[idx]
        _src = content['src']

        img_response = requests.get(_src)
        save_filepath = os.path.join(tmp_dir, str(i_count) + '.jpg')

        open(save_filepath, 'wb').write(img_response.content)

        i_count = i_count + 1

    pdf_bytes = img2pdf.convert([
        Image.open(os.path.join(tmp_dir, j))
            .filename for j in natsorted(os.listdir(tmp_dir)) if j.endswith('jpg')
        ])

    shutil.rmtree(tmp_dir)

    return Response(content=pdf_bytes, media_type="application/pdf")