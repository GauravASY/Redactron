import gradio as gr


with gr.Blocks() as demo:
    gr.Markdown( "# PII Redaction")
    upload = gr.UploadButton(
        label="Upload Doc",
        file_types=["pdf", "txt", "docx"],
        size = "md",
    )
    

def main():
    demo.launch()
    


if __name__ == "__main__":
    main()
