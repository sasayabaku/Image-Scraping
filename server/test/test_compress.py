import sys

sys.path.append("/src/")
sys.path.append("../src/")

import requests


def test_compress_pdf():

    pdf_file_path = "./assets/testpdf.pdf"

    with open(pdf_file_path, "rb") as pdf_file:

        files = {"file": (pdf_file_path, pdf_file, "application/pdf")}

        response = requests.post("http://localhost:9999/compress-pdf", files=files)

        assert type(response.content) == bytes
