from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import jinja2

app = FastAPI(title="Emergencias Eléctricas EL TATA")

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar Jinja2
template_dir = Path(__file__).parent.parent / "templates"
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(str(template_dir)),
    autoescape=jinja2.select_autoescape(['html', 'xml'])
)

# ============ DATOS DE GENERADORES PARA ALQUILER ============
generadores = [
    {
        "id": 1,
        "nombre": "Grupo Electrógeno 80 kVA",
        "descripcion": "Potencia ideal para comercios, eventos medianos y edificios de departamentos.",
        "precio": "A convenir",
        "categoria": "trifásico",
        "imagen": "generador3.webp",
        "rating": 4.9,
        "caracteristicas": [
            "Motor de alta eficiencia",
            "Cabina insonorizada",
            "Tablero digital con monitoreo",
            "Autonomía extendida"
        ]
    },
    {
        "id": 2,
        "nombre": "Grupo Electrógeno 120 kVA",
        "descripcion": "Equilibrio perfecto entre potencia y eficiencia para industrias y eventos grandes.",
        "precio": "A convenir",
        "categoria": "trifásico",
        "imagen": "generador4.webp",
        "rating": 4.9,
        "caracteristicas": [
            "Motor diésel de alta eficiencia",
            "Cabina insonorizada",
            "Monitoreo digital avanzado",
            "Tanque de combustible de gran capacidad"
        ]
    },
    {
        "id": 3,
        "nombre": "Grupo Electrógeno 150 kVA",
        "descripcion": "Máxima potencia para obras, supermercados y centros comerciales.",
        "precio": "A convenir",
        "categoria": "trifásico",
        "imagen": "generador5.webp",
        "rating": 4.8,
        "caracteristicas": [
            "Motor de alto rendimiento",
            "Cabina insonorizada premium",
            "Sistema de monitoreo en tiempo real",
            "Arranque automático"
        ]
    },
    {
        "id": 4,
        "nombre": "Grupo Electrógeno 180 kVA",
        "descripcion": "Potencia industrial para proyectos exigentes y emergencias críticas.",
        "precio": "A convenir",
        "categoria": "trifásico",
        "imagen": "generador6.webp",
        "rating": 4.9,
        "caracteristicas": [
            "Motor de última generación",
            "Cabina insonorizada de alto nivel",
            "Tablero digital con telemetría",
            "Autonomía para trabajo continuo"
        ]
    },
    {
        "id": 5,
        "nombre": "Grupo Electrógeno 100 kVA",
        "descripcion": "Versatilidad y confianza para eventos corporativos y catering.",
        "precio": "A convenir",
        "categoria": "trifásico",
        "imagen": "generador7.webp",
        "rating": 4.7,
        "caracteristicas": [
            "Motor eficiente",
            "Bajo nivel de ruido",
            "Fácil instalación",
            "Monitoreo básico"
        ]
    }
]

# ============ SERVICIOS ADICIONALES ============
servicios = [
    {
        "icono": "fa-truck",
        "titulo": "Logística Propia",
        "descripcion": "Traslado e instalación en el lugar con flota especializada."
    },
    {
        "icono": "fa-headset",
        "titulo": "Guardia 24/7",
        "descripcion": "Asistencia técnica telefónica y presencial ante cualquier imprevisto."
    },
    {
        "icono": "fa-tools",
        "titulo": "Mantenimiento Preventivo",
        "descripcion": "Equipos con service preventivo al día para garantizar confiabilidad."
    },
    {
        "icono": "fa-plug",
        "titulo": "Cables y Accesorios",
        "descripcion": "Alquiler de cables de potencia y tableros de transferencia."
    }
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    try:
        template = env.get_template("index.html")
        content = template.render(
            generadores=generadores,
            servicios=servicios,
            empresa="Emergencias Eléctricas EL TATA",
            telefono="+54 11 5339-2457",
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
                <p><strong>Solución:</strong> Verifica que la carpeta <code>templates</code> contiene <code>index.html</code></p>
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