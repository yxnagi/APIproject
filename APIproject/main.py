import logging
import os
from pathlib import Path
from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from APIproject.core.weather import Weather

logs_file = Path(Path().resolve(), "log.txt")
logs_file.touch(exist_ok=True)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=os.environ.get("LOGLEVEL", "INFO"),
    handlers=[logging.FileHandler(logs_file), logging.StreamHandler()],
)

log = logging.getLogger(__name__)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

weather = Weather()

@app.get("/")
async def root():
    log.info("gone to root")
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    log.info(f"loaded item {item_id}")
    return {"item_id": item_id}


@app.get("/weather")
def get_weather(latitude: float = 51.5002, longitude: float = -0.120000124, options:str = "temperature_2m"):
    log.info(f"Requested latitude: {latitude} and longitude: {longitude} with options {options}")
    output = weather.get_weather(latitude=latitude, longitude=longitude, options=options)
    return {"weather": output}


@app.get("/html", response_class=HTMLResponse)
def html_output(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "data": ["hello", 1, False]},
    )

@app.get("/chart", response_class=HTMLResponse)
def html_output(request: Request):
    return templates.TemplateResponse(
        "weather.html",
        {"request": request, "data": get_weather(options="temperature_2m")},
    )