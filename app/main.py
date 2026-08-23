from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

app = FastAPI()

# Configurar Jinja2 SIN CACHE
env = Environment(
    loader=FileSystemLoader("templates"),
    auto_reload=True  # Esto evita problemas de cache
)

generadores = [
    {"nombre": "Generador 3000W", "descripcion": "Potencia para tu hogar", "precio": "$1,299"},
    {"nombre": "Generador 5000W", "descripcion": "Potencia industrial", "precio": "$2,499"}
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    template = env.get_template("index.html")
    content = template.render(request=request, generadores=generadores)
    return HTMLResponse(content=content)