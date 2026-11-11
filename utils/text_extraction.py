import pymupdf
import logging

def pdf_extractor(docs):
    logging.info("Extracting information from PDF....")
    pdf_doc = pymupdf.open(docs)
    total_text =""
    for pages in range(len(pdf_doc)):
        text = pdf_doc[pages].get_text().encode('utf-8')
        images = pdf_doc[pages].get_images(full=True)
        #implement text extraction from the images

        total_text += str(text)
    logging.info("Information Extraction is complete....")
    return total_text