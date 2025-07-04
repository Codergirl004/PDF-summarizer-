import gradio as gr
import shutil
import os
import requests

SHARED_PDF_PATH = "shared/last.pdf"
BACKEND_JSON_URL = "http://127.0.0.1:8000/process_json"

def upload_and_process(pdf_file):
    os.makedirs("shared", exist_ok=True)
    shutil.copy(pdf_file.name, SHARED_PDF_PATH)

    try:
        response = requests.get(BACKEND_JSON_URL, timeout=120)
        data = response.json()

        if "error" in data:
            return f"❌ {data['error']}", "", ""

        return "✅ File processed successfully!", data["summary"], data["highlights"]

    except Exception as e:
        return f"❌ Error contacting backend: {e}", "", ""

custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

body, .gradio-container {
    font-family: 'Poppins', sans-serif !important;
    background: linear-gradient(135deg, #e8e0f4, #f8f0ff) !important;
    min-height: 100vh !important;
}

.gr-button {
    background-color: #7e57c2 !important; /* Solid Purple */
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 12px 24px !important;
    font-weight: 600;
    font-size: 16px;
}

.gr-textbox, .gr-file {
    border-radius: 12px !important;
    border: 1px solid #ccc !important;
    background: #ffffffdd !important;
}
#upload-btn {
    background-color: #7e57c2 !important;  /* Purple */
    color: white !important;               /* White text */
    border: none !important;
    border-radius: 12px !important;
    padding: 12px 24px !important;
    font-weight: 600;
    font-size: 16px;
    transition: 0.3s ease-in-out;
}

#upload-btn:hover {
    background-color: #6a4bbf !important;
    cursor: pointer;
}

.gradio-container {
    padding: 30px !important;
}
"""

with gr.Blocks(css=custom_css) as demo:
    gr.HTML("""
        <div style='text-align: center; margin-bottom: 20px;'>
            <h1 style='color: #5a4e82; font-size: 2.4rem;'> PDF Summarizer & Highlight Extractor</h1>
            <p style='color: #6e5b96; font-size: 1rem;'>Upload once. Extract insights instantly using Groq LLMs.</p>
        </div>
    """)

    with gr.Row():
        pdf_input = gr.File(label=" Upload your PDF", file_types=[".pdf"])

    upload_btn = gr.Button(" Upload & Summarize", elem_id="upload-btn")


    status = gr.Textbox(label="⚙️ Status", interactive=False, max_lines=2)

    with gr.Row():
        summary_box = gr.Textbox(label="📝 Summary", lines=15, show_copy_button=True)
        highlight_box = gr.Textbox(label="✨ Highlights", lines=15, show_copy_button=True)

    upload_btn.click(upload_and_process, inputs=[pdf_input], outputs=[status, summary_box, highlight_box])

demo.launch()
