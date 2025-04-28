import io
from pypdf import PdfReader, PdfWriter


def compress_pdf(input_file, power=0):
    """
    Function to compress PDF file

    params:
        input_file: input PDF byte
        output_file: output PDF byte
        power: compress level (0: low, 1: middle, 2: high)
    """

    pdf_byte = io.BytesIO(input_file)
    pdf_reader = PdfReader(pdf_byte)
    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    pdf_writer.compress_content_streams = True

    # for page in pdf_writer.pages:
    #     for img in page.images:
    #         if hasattr(img, "filter_decodeparms"):
    #             if "/ColorTransform" in img.filter_decodeparms:
    #                 img.filter_decodeparms["/ColorTransform"] = 1

    output_bytes_stream = io.BytesIO()
    pdf_writer.write(output_bytes_stream)
    output_bytes = output_bytes_stream.getvalue()

    return output_bytes
