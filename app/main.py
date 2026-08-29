from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import jinja2

app = FastAPI(title="GenPower", description="Energía que impulsa tu mundo")

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar Jinja2
template_dir = Path(__file__).parent.parent / "templates"
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(str(template_dir)),
    autoescape=jinja2.select_autoescape(['html', 'xml'])
)

# Datos de generadores con imágenes
generadores = [
    {
        "id": 1, 
        "nombre": "Generador 3000W", 
        "descripcion": "Potencia silenciosa para tu hogar con tecnología de última generación",
        "precio": "$1,299", 
        "categoria": "hogar",
        "imagen": "generator-3000w.jpg",
        "rating": 4.8,
        "caracteristicas": ["Motor 4 tiempos eficiente", "Nivel de ruido 58dB", "Autonomía 10 horas", "Arranque eléctrico"]
    },
    {
        "id": 2, 
        "nombre": "Generador 5000W", 
        "descripcion": "Potencia industrial para proyectos exigentes y construcción",
        "precio": "$2,499", 
        "categoria": "industrial",
        "imagen": "generator-5000w.jpg",
        "rating": 4.9,
        "caracteristicas": ["Motor diésel turbo", "Alta eficiencia energética", "Arranque eléctrico", "Autonomía 24 horas"]
    },
    {
        "id": 3, 
        "nombre": "Generador Portátil 2000W", 
        "descripcion": "Ligero y potente para camping, viajes y emergencias",
        "precio": "$899", 
        "categoria": "portátil",
        "imagen": "generator-portatil.jpg",
        "rating": 4.7,
        "caracteristicas": ["Peso 22kg", "Motor 4 tiempos", "Ultra silencioso", "Ideal para viajes"]
    },
    {
        "id": 4, 
        "nombre": "Generador Eco 1500W", 
        "descripcion": "Tecnología ecológica con mínimo consumo de combustible",
        "precio": "$1,099", 
        "categoria": "ecológico",
        "imagen": "generator-eco.jpg",
        "rating": 4.6,
        "caracteristicas": ["Motor eficiente", "Bajas emisiones CO2", "Larga duración", "Silencioso"]
    },
    {
        "id": 5, 
        "nombre": "Generador Tech 4000W", 
        "descripcion": "Conectividad WiFi y control remoto desde tu smartphone",
        "precio": "$1,899", 
        "categoria": "tecnología",
        "imagen": "generator-tech.jpg",
        "rating": 4.9,
        "caracteristicas": ["Control remoto WiFi", "App móvil", "Monitoreo en tiempo real", "Auto-arranque"]
    },
    {
        "id": 6, 
        "nombre": "Generador Emergencia 2500W", 
        "descripcion": "Diseñado para situaciones críticas con arranque inmediato",
        "precio": "$1,499", 
        "categoria": "emergencia",
        "imagen": "generator-emergencia.jpg",
        "rating": 4.8,
        "caracteristicas": ["Arranque inmediato", "Batería de respaldo", "Sistema de seguridad", "Autonomía 8h"]
    }
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    try:
        template = env.get_template("index.html")
        content = template.render(
            generadores=generadores,
            empresa="GenPower",
            año="2026"
        )
        return HTMLResponse(content=content)
    except Exception as e:
        return HTMLResponse(content=f"""
        <!DOCTYPE html>
        <html>
        <head><title>Error</title></head>
        <body style="font-family: Arial; padding: 40px; background: #f5f5f5;">
            <h1 style="color: #d32f2f;">Error al cargar la página</h1>
            <div style="background: white; padding: 20px; border-radius: 8px;">
                <p><strong>Error:</strong> {str(e)}</p>
                <p><strong>Solución:</strong> Verifica que la carpeta <code>templates</code> existe y contiene <code>index.html</code></p>
            </div>
        </body>
        </html>
        """, status_code=500)

@app.get("/api/generador/{generador_id}")
async def get_generador(generador_id: int):
    for g in generadores:
        if g["id"] == generador_id:
            return g
    return {"error": "Generador no encontrado"}

@app.get("/api/filtrar/{categoria}")
async def filtrar_generadores(categoria: str):
    if categoria == "todos":
        return generadores
    resultado = [g for g in generadores if g["categoria"] == categoria]
    return resultado