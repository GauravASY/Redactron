from utils.types import regex_types
import re
import logging

def regex_redactor(text):
    logging.info("Redacting text using regex")
    redacted_text = text
    for key, value in regex_types.items():
        redacted_text = re.sub(value, "[REDACTED]", redacted_text)
    return redacted_text