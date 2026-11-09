import gradio as gr
from fastapi import FastAPI
import logging,uvicorn
from utils.text_extraction import pdf_extractor


app = FastAPI()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

def redaction(docs):
    logging.info(f"The document uploaded is : \n{docs}")
    total_text = ""
    try:
        if docs.endswith(".pdf"):
            return pdf_extractor(docs)
        else:
            logging.info("The uploaded document is not a pdf file")
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
