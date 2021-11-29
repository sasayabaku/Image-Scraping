import sys
sys.path.append('/src/')
sys.path.append('../src/')

from scraping import listup_image

import requests

TARGET_URL = "https://www.irasutoya.com/"

_uuid = None

def test_listup():
    assert len(listup_image(TARGET_URL)) > 0
    assert listup_image("https://none.example.com/") == False

def test_api_listup():
    global _uuid
    
    response = requests.post(
        "http://localhost:9999/listup",
        json={
            "url": TARGET_URL
        }
    )

    _uuid = response.json()['connection_id']

    assert len(response.json()['img_list']) > 0

def test_api_generate_pdf():
    global _uuid
    
    response = requests.post(
        "http://localhost:9999/generate",
        json={
            "uuid": _uuid,
            "indexes": [0, 1]
        }
    )

    assert type(response.content) == bytes