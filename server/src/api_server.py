from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import redis
import uuid
import json

from scraping import listup_image

REDIS_SERVER_NAME = "redis"

class UrlItem(BaseModel):
    url: str

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