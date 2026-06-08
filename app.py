from flask import Flask, render_template
import os

app = Flask(__name__)

APPS = [
    {
        "id": "sghn",
        "nombre": "Gestión de Horarios y Nómina",
        "descripcion": "Generación automática de horarios, asignación de profesores, nómina docente y exportación a Excel.",
        "icono": "🗓️",
        "color": "#1565C0",
        "url": os.environ.get("URL_SGHN", "https://web-production-430f8.up.railway.app"),
        "estado": "activo",
        "tags": ["Horarios", "Nómina", "Profesores"],
    },
    {
        "id": "seguimiento",
        "nombre": "Seguimiento a Estudiantes",
        "descripcion": "Registro y seguimiento del desempeño académico, alertas tempranas y gestión de casos por docente.",
        "icono": "🎓",
        "color": "#00695C",
        "url": os.environ.get("URL_SEGUIMIENTO", "https://ruta-academica-teleco.up.railway.app/"),
        "estado": "activo",
        "tags": ["Estudiantes", "Seguimiento", "Alertas"],
    },
    {
        "id": "actividades-docentes",
        "nombre": "Seguimiento Actividades Docentes",
        "descripcion": "Control de funciones administrativas, cumplimiento de actividades y carga no lectiva por docente.",
        "icono": "📋",
        "color": "#6A1B9A",
        "url": os.environ.get("URL_ACTIVIDADES_DOCENTES", "https://seg-intersemestral.up.railway.app/"),
        "estado": "activo",
        "tags": ["Docentes", "Actividades", "Gestión"],
    },
    {
        "id": "gestion-academica",
        "nombre": "Gestión Académica",
        "descripcion": "Módulos integrados para la gestión de investigación, proyección social y procesos de calidad del programa.",
        "icono": "🏛️",
        "color": "#B71C1C",
        "url": "#",
        "estado": "pronto",
        "tags": ["Investigación", "Proyección Social", "Calidad"],
        "submodulos": [
            {"nombre": "Investigación",     "icono": "🔬", "color": "#1565C0", "url": os.environ.get("URL_INVESTIGACION", "#")},
            {"nombre": "Proyección Social", "icono": "🤝", "color": "#2E7D32", "url": os.environ.get("URL_PROYECCION",    "#")},
            {"nombre": "Calidad",           "icono": "🏆", "color": "#E65100", "url": os.environ.get("URL_CALIDAD",       "#")},
        ],
    },
]

@app.route("/")
def index():
    return render_template("index.html", apps=APPS)

@app.route("/health")
def health():
    return {"ok": True}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
