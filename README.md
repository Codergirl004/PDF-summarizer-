📄 PDF Summarizer & Highlight Extractor
Upload a PDF once via a beautiful Gradio interface and instantly extract a clean summary and highlights using powerful Groq/OpenRouter LLMs. Results are also viewable on a FastAPI backend.


Features
✅ Upload PDF once (no duplicate sending)

🧠 Get LLM-powered summary & highlights

🎨 Beautiful lavender-themed frontend

🔁 FastAPI backend with /latest and /process_json

💾 Local file handling, no cloud upload


📦 Tech Stack
FastAPI

Gradio

Groq/OpenRouter LLMs

Python Libraries: requests, fpdf, PyMuPDF, shutil



Project Structure:
📂 pdf-summarizer/
  main.py (FastAPI backend)
  ui.py (Gradio frontend)
  summarizer.py (Text extraction + LLM logic)
  requirements.txt


⚙️ Installation
git clone https://github.com/your-username/pdf-summarizer.git
cd pdf-summarizer

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies

pip install -r requirements.txt

▶️ Running the App


In Terminal 1 (FastAPI backend):
uvicorn main:app --reload

In Terminal 2 (Gradio frontend):
python ui.py


🔗 API Endpoints
Endpoint	Description	Format

/	Welcome screen	HTML

/process_json	Process PDF, return summary

/highlights	JSON

/latest	View summary & highlights (browser)	HTML





