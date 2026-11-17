from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from workers import WorkerEntrypoint, asgi

app = FastAPI()


@app.get("/")
async def read_root():
    html_content = Path("index.html").read_text(encoding="utf-8")
    return HTMLResponse(content=html_content, status_code=200)
<<<<<<< HEAD

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        return await asgi.fetch(app, request, self.env)
=======
>>>>>>> parent of fcdcd40 (Update main.py)
