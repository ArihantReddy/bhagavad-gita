from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.services.quote_service import QuoteService


app = FastAPI(
    title="Bhagavad Gita QR Quotes API",
    description="Displays a random Bhagavad Gita quote each time the application is accessed.",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

quote_service = QuoteService()


@app.get("/", response_class=HTMLResponse)
def get_quote(request: Request):
    quote = quote_service.get_random_quote()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "quote": quote
        }
    )


@app.get("/health", response_class=JSONResponse)
def health():
    return {
        "status": "healthy",
        "application": "Bhagavad Gita QR Quotes",
        "version": "1.0.0"
    }