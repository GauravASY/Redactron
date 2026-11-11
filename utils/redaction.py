from utils.types import regex_types
import re
import logging
import spacy

def regex_redactor(text):
    logging.info("Redacting text using regex")
    redacted_text = text
    for key, value in regex_types.items():
        redacted_text = re.sub(value, f'{key.upper()}: [--XXXXXX--]', redacted_text)
    return redacted_text


def ner_redactor(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    redacted_text = text
    for ent in doc.ents:
        if ent.label_ in ["NAME","PERSON","LOC","GPE","ORG","DATE"]:
            redacted_text = redacted_text.replace(ent.text, f'{ent.label_}: [--XXXXXX--]')
    return redacted_text
