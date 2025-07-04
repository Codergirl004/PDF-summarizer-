from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from summarizer import extract_text_from_pdf, summarize_text, extract_highlights
import os

app = FastAPI()

SHARED_PDF_PATH = "shared/last.pdf"
latest_result = {
    "filename": "last.pdf",
    "summary": "",
    "highlights": ""
}


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <h2>📄 PDF Summarizer API</h2>
    <ul>
        <li><a href="/latest">View Latest Summary (HTML)</a></li>
        <li><a href="/process_json">Get Latest Summary (JSON)</a></li>
    </ul>
    """


@app.get("/process_json")
def process_shared_pdf_json():
    """Returns summary and highlights from last uploaded PDF (JSON)."""
    if not os.path.exists(SHARED_PDF_PATH):
        return {"error": "No PDF found. Please upload one via Gradio."}

    try:
        text = extract_text_from_pdf(SHARED_PDF_PATH)
        summary = summarize_text(text)
        highlights = extract_highlights(text)

        # Save to global cache
        latest_result.update(
            summary=summary,
            highlights=highlights
        )

        return {
            "summary": summary,
            "highlights": highlights
        }

    except Exception as e:
        return {"error": str(e)}


@app.get("/latest", response_class=HTMLResponse)
def get_latest_html():
    """View latest summary + highlights in the browser."""
    if not latest_result["summary"]:
        return "<h3>❌ No summary available. Upload and process a PDF first.</h3>"

    return f"""
    <h2>📄 File: {latest_result['filename']}</h2>
    <h3>📝 Summary</h3>
    <p>{latest_result['summary'].replace('\n', '<br>')}</p>
    <h3>✨ Highlights</h3>
    <p>{latest_result['highlights'].replace('\n', '<br>')}</p>
    """
