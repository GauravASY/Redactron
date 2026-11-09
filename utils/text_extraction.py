import pymupdf
import logging

def pdf_extractor(docs):
    pdf_doc = pymupdf.open(docs)
    total_text =""
    for pages in range(len(pdf_doc)):
        text = pdf_doc[pages].get_text().encode('utf-8')
        images = pdf_doc[pages].get_images(full=True)
        total_text += str(text)
    return total_text