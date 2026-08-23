from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# Configurar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar templates
templates = Jinja2Templates(directory="templates")

# DATOS DE GENERADORES (Agrega todos los que necesites)
GENERADORES = [
    {
        "id": 1,
        "nombre": "Generador Eléctrico 3000W",
        "descripcion": "Ideal para hogares y pequeños negocios. Motor silencioso y eficiente con arranque eléctrico.",
        "caracteristicas": [
            "3000W de potencia máxima",
            "Motor 4 tiempos OHV",
            "Autonomía 8 horas",
            "Nivel de ruido 58dB",
            "Arranque eléctrico y manual",
            "Tanque de 15 litros"
        ],
        "imagen": "generador1.jpg",
        "precio": "$1,299.99",
        "categoria": "Hogar"
    },
    {
        "id": 2,
        "nombre": "Generador Industrial 5000W",
        "descripcion": "Potencia para obras, talleres y grandes instalaciones. Resistente y duradero para uso profesional.",
        "caracteristicas": [
            "5000W de potencia máxima",
            "Motor diesel 4 tiempos",
            "Arranque eléctrico",
            "Tanque 25 litros",
            "Autonomía 12 horas",
            "Panel de control digital"
        ],
        "imagen": "generador2.jpg",
        "precio": "$2,499.99",
        "categoria": "Industrial"
    },
    {
        "id": 3,
        "nombre": "Generador Portátil 1500W",
        "descripcion": "Perfecto para camping, viajes y emergencias. Ligero y compacto para llevar a cualquier parte.",
        "caracteristicas": [
            "1500W de potencia máxima",
            "Motor 2 tiempos",
            "Peso 12 kg",
            "Batería recargable",
            "Autonomía 6 horas",
            "Silencioso 52dB"
        ],
        "imagen": "generador3.jpg",
        "precio": "$899.99",
        "categoria": "Portátil"
    },
    {
        "id": 4,
        "nombre": "Generador Silencioso 2000W Inverter",
        "descripcion": "Tecnología inverter para corriente estable. Ideal para equipos electrónicos y computadoras.",
        "caracteristicas": [
            "2000W de potencia",
            "Tecnología Inverter",
            "Nivel de ruido 48dB",
            "Salida USB y 12V",
            "Arranque eléctrico",
            "Peso 18 kg"
        ],
        "imagen": "generador4.jpg",
        "precio": "$1,699.99",
        "categoria": "Tecnología"
    },
    {
        "id": 5,
        "nombre": "Generador Solar Híbrido 1000W",
        "descripcion": "Sistema híbrido solar-gasolina. Energía limpia y eficiente para el hogar.",
        "caracteristicas": [
            "1000W de potencia",
            "Panel solar incluido",
            "Batería de litio 12V",
            "Autonomía 10 horas",
            "Carga USB y AC",
            "Ecológico y silencioso"
        ],
        "imagen": "generador5.jpg",
        "precio": "$2,999.99",
        "categoria": "Ecológico"
    },
    {
        "id": 6,
        "nombre": "Generador de Emergencia 3500W",
        "descripcion": "Diseñado para situaciones de emergencia y apagones. Fácil de usar y mantener.",
        "caracteristicas": [
            "3500W de potencia",
            "Motor 4 tiempos",
            "Arranque manual",
            "Tanque 20 litros",
            "Autonomía 9 horas",
            "Chasis con ruedas"
        ],
        "imagen": "generador6.jpg",
        "precio": "$1,499.99",
        "categoria": "Emergencia"
    }
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "generadores": GENERADORES
    })

@app.get("/api/generador/{id}")
async def get_generador(id: int):
    for g in GENERADORES:
        if g["id"] == id:
            return g
    return {"error": "Generador no encontrado"}

@app.get("/api/categoria/{categoria}")
async def get_por_categoria(categoria: str):
    resultados = [g for g in GENERADORES if g["categoria"].lower() == categoria.lower()]
    return resultados