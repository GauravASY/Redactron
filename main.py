import gradio as gr
from fastapi import FastAPI
import logging,uvicorn
from utils.text_extraction import pdf_extractor
from utils.redaction import regex_redactor, ner_redactor

app = FastAPI()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

def redaction(docs):
    logging.info(f"The document uploaded is : \n{docs}")
    redacted_regex_text = ""
    redacted_ner_text = ""
    try:
        if docs.endswith(".pdf"):
            extracted_text = pdf_extractor(docs)
            redacted_regex_text = regex_redactor(extracted_text)
            redacted_ner_text = ner_redactor(redacted_regex_text)
        else:
            logging.info("The uploaded document is not a pdf file")
    except Exception as e:
        logging.error(f"Error in redaction function : \n{e}")
    return redacted_ner_text

# Gradio UI for uplaoding the documents
with gr.Blocks() as demo:
    gr.Markdown( "# PII Redaction")
    upload = gr.File(
        label="Upload Doc",
        file_types=[".pdf", ".txt", ".docx"],
        type="filepath",
        file_count="single",
    )
    submit = gr.Button("Submit", variant="primary", size = "md")
    
    output_markdown = gr.Markdown(label="Redacted Doc")

    submit.click(fn=redaction,
    inputs=upload,
    outputs=output_markdown
    )

# Mounting the gradio on FastAPI instance at "/"
gr.mount_gradio_app(app, demo, path= "/")
def main():
    uvicorn.run("main:app", reload=True)
    


if __name__ == "__main__":
    main()
