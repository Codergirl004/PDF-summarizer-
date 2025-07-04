import fitz  # PyMuPDF
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()
client = Groq(api_key="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")


MODEL = "llama3-8b-8192"


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    return "".join(page.get_text() for page in doc)

def _ask_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()

def summarize_text(text: str) -> str:
    prompt = f"Summarize the following text in a paragraph:\n\n{text[:3000]}"
    return _ask_llm(prompt)

def extract_highlights(text: str) -> str:
    prompt = f"Extract bullet point highlights from this document:\n\n{text[:3000]}"
    return _ask_llm(prompt)
