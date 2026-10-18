from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()


@app.get("/")
def read_root():
    html_content = Path("index.html").read_text(encoding="utf-8")
    return HTMLResponse(content=html_content, status_code=200)
