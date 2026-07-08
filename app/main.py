from fastapi import FastAPI
from app.services.quote_service import QuoteService
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Bhagavad Gita Quotes API",
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