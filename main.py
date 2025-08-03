from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routes import orders
from app.utils.date_utils import format_brazilian_date, format_brazilian_datetime

app = FastAPI()

app.include_router(orders.router)

# pages
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# dd/mm/yyyy
templates.env.filters["brazilian_date"] = format_brazilian_date
templates.env.filters["brazilian_datetime"] = format_brazilian_datetime

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
