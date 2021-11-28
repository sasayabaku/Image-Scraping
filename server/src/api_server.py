from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from scraping import listup_image


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

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/listup")
async def get_listup(url: UrlItem):
    img_list = listup_image(url=url.url)
    return {"img_list": img_list}