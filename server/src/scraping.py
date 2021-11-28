import os
import shutil
import img2pdf
from natsort import natsorted
from PIL import Image
import requests
from requests.api import request
from tqdm import tqdm
from bs4 import BeautifulSoup
from random import randint, random
import argparse

def random_generate(n):
    range_start = 10**(n-1)
    range_end = 10**n - 1
    return randint(range_start, range_end)

def listup_image(url, keyword=None):

    tmp_dir = "./tmp"
    pdf_file = str(random_generate(20)) + '.pdf'

    os.makedirs(tmp_dir, exist_ok=True)

    try:
        response = requests.get(url)
    except:
        return False

    soup = BeautifulSoup(response.text, 'html.parser')

    # 画像リスト作成
    img_list = [{
        'src': i.attrs['src'], 
        'alt': i.attrs['alt'] if 'alt' in i.attrs.keys() else None, 
        'class': i.attrs['class'] if 'class' in i.attrs.keys() else None
        } for i in soup.select('img')]

    return img_list

def total(url, keyword=None):

    tmp_dir = "./tmp"
    pdf_file = str(random_generate(20)) + '.pdf'

    os.makedirs(tmp_dir, exist_ok=True)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    i_count = 0
    for image in tqdm(soup.select('img')):

        try:
            if not keyword in image.attrs['class']:
                if not keyword in image.attrs['alt']:
                    continue
        except:
            continue

        img_src = image.attrs['src']
        img_response = requests.get(img_src)

        save_filepath = os.path.join(tmp_dir, str(i_count) + '.jpg')

        open(save_filepath, 'wb').write(img_response.content)

        i_count = i_count + 1

    with open(pdf_file, 'wb') as f:
        f.write(img2pdf.convert([
            Image.open(os.path.join(tmp_dir, j))
                .filename for j in natsorted(os.listdir(tmp_dir)) if j.endswith('jpg')
        ]))

    shutil.rmtree(tmp_dir)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Web Page Scraping")

    parser.add_argument('url', help='Page URL')
    parser.add_argument('--keyword', help="Exclude Keyword", default=None)

    args = parser.parse_args()

    total(args.url, keyword=args.keyword)