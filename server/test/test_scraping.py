import sys
sys.path.append('/src/')
sys.path.append('../src/')

from scraping import listup_image

import requests

TARGET_URL = "https://www.irasutoya.com/"


def test_listup():
    assert len(listup_image(TARGET_URL)) > 0
    assert listup_image("https://none.example.com/") == False

def test_api_listup():
    
    response = requests.post(
        "http://localhost:9999/listup",
        json={
            "url": TARGET_URL
        }
    )

    assert len(response.json()['img_list']) > 0