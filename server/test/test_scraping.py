import sys
sys.path.append('/src/')

from scraping import listup_image



def test_listup():
    assert len(listup_image("https://www.irasutoya.com/")) > 0
    assert listup_image("https://none.example.com/") == False