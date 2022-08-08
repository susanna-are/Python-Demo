from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    cities = [ { 'name': 'Dallas', 'temperature':'50F'}, { 'name': 'New York','temperature': '39F'} ,{'name': 'Mexico name','temperature': '69F'} , {'name': 'Vancouver','temperature':'45F'} , {'name': 'Sao Paulo','temperature':'76F'} , {'name': 'Buenos Aires','temperature':'85F'} , {'name': 'Frankfurt','temperature': '45F'} , {'name': 'Paris','temperature': '53F'} , {'name': 'Madrid','temperature':'42F'} , {'name': 'Berlin','temperature':'45F'} , {'name': 'Moscow','temperature': '15F'} ,{'name': 'Delhi','temperature':'54F'} ,{'name': 'Beijing','temperature':'22F'} , {'name': 'Tokyo','temperature': '33F'} , {'name': 'Sydney','temperature': '60F'} ]
    return templates.TemplateResponse("item.html", {"request": request, "cities": cities})