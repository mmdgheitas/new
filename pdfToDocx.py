from pdf2docx import Converter


docx_path = "vira.docx"

pdf_path = "test.pdf"


cv = Converter(pdf_path)

cv.convert(docx_path)

cv.close()