import gradio as gr
from fastapi import FastAPI
import pymupdf, logging
import uvicorn


app = FastAPI()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

def redaction(docs):
    logging.info(f"The document uploaded is : \n{docs}")
    try:
        pdf_doc = pymupdf.open(docs)
        logging.info(pdf_doc) 
    except Exception as e:
        logging.error(f"Error in redaction function : \n{e}")

# Gradio UI for uplaoding the documents
with gr.Blocks() as demo:
    gr.Markdown( "# PII Redaction")
    upload = gr.UploadButton(
        label="Upload Doc",
        file_types=[".pdf", ".txt", ".docx"],
        size = "md",
    )
    upload.click(fn=redaction,
    inputs=upload,
    outputs=gr.Textbox(
        label="Redacted Doc",
        lines=10
    ))

# Mounting the gradio on FastAPI instance at "/"
gr.mount_gradio_app(app, demo, path= "/")
def main():
    uvicorn.run("main:app", reload=True)
    


if __name__ == "__main__":
    main()
