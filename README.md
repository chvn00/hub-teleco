# Hub — Facultad de Ingeniería de Telecomunicaciones · USTA

Portal web centralizado para las herramientas académicas y administrativas de la Facultad de Ingeniería de Telecomunicaciones de la Universidad Santo Tomás.

## ¿Qué es?

Una app Flask ligera desplegada en Railway que funciona como página de inicio unificada para todas las aplicaciones de la facultad. Cada herramienta sigue corriendo de forma independiente en su propio servicio; el hub las presenta en un solo lugar con acceso directo.

## Herramientas incluidas

| # | Nombre | Estado | Variable de entorno |
|---|--------|--------|---------------------|
| 1 | **Gestión de Horarios y Nómina (SGHN)** | Activo | `URL_SGHN` |
| 2 | **Seguimiento a Estudiantes** | Próximamente | `URL_SEGUIMIENTO` |
| 3 | **Seguimiento Actividades Docentes** | Próximamente | `URL_ACTIVIDADES_DOCENTES` |
| 4 | **Gestión Académica** | Próximamente | — |
| ↳ | Investigación | Próximamente | `URL_INVESTIGACION` |
| ↳ | Proyección Social | Próximamente | `URL_PROYECCION` |
| ↳ | Calidad | Próximamente | `URL_CALIDAD` |

## Estructura del proyecto

```
hub-teleco/
├── app.py               # Flask app — lista de herramientas (APPS)
├── requirements.txt     # flask, gunicorn
├── Procfile             # Comando de arranque para Railway
├── .gitignore
├── static/
│   └── escudo.gif       # Escudo institucional USTA
└── templates/
    └── index.html       # Portal completo (Bootstrap 5 + Bootstrap Icons)
```

## Agregar una nueva herramienta

Edita la lista `APPS` en `app.py`:

```python
{
    "id": "mi-app",
    "nombre": "Nombre visible en el portal",
    "descripcion": "Descripción breve de qué hace la herramienta.",
    "icono": "bi-nombre-icono",        # Bootstrap Icons
    "color": "#1565C0",                # Color principal de la card
    "url": os.environ.get("URL_MI_APP", "#"),
    "estado": "activo",                # "activo" | "pronto"
    "tags": ["Tag1", "Tag2"],
},
```

Para herramientas con submódulos (como Gestión Académica):

```python
{
    "id": "mi-app-multi",
    "nombre": "Nombre",
    "descripcion": "Descripción.",
    "icono": "bi-layers",
    "color": "#B71C1C",
    "url": "#",
    "estado": "pronto",
    "tags": ["Tag1", "Tag2", "Tag3"],
    "submodulos": [
        {"nombre": "Módulo A", "icono": "bi-journal-richtext", "color": "#1565C0", "url": os.environ.get("URL_MODULO_A", "#")},
        {"nombre": "Módulo B", "icono": "bi-people",           "color": "#2E7D32", "url": os.environ.get("URL_MODULO_B", "#")},
        {"nombre": "Módulo C", "icono": "bi-patch-check",      "color": "#E65100", "url": os.environ.get("URL_MODULO_C", "#")},
    ],
},
```

## Activar una herramienta en Railway

Cuando una app pasa de *Próximamente* a *Activo*:

1. En Railway → servicio `hub-teleco` → **Variables** → agregar la variable correspondiente:
   ```
   URL_SGHN=https://gestionteleco.up.railway.app
   ```
2. Cambiar `"estado": "pronto"` → `"estado": "activo"` en `app.py`.
3. Hacer `git push` — Railway redespliega automáticamente.

## Correr localmente

```bash
cd hub-teleco
pip install -r requirements.txt
python app.py
# → http://localhost:5000
```

## Despliegue en Railway

1. Crear nuevo servicio en Railway → **Deploy from GitHub repo** → `chvn00/hub-teleco`
2. Railway detecta el `Procfile` automáticamente
3. Agregar las variables de entorno de cada app activa
4. (Opcional) Cambiar el dominio en **Settings → Networking** al subdominio deseado

## Variables de entorno

| Variable | Descripción |
|----------|-------------|
| `URL_SGHN` | URL del servicio de Gestión de Horarios y Nómina |
| `URL_SEGUIMIENTO` | URL del servicio de Seguimiento a Estudiantes |
| `URL_ACTIVIDADES_DOCENTES` | URL del servicio de Seguimiento Actividades Docentes |
| `URL_INVESTIGACION` | URL del módulo de Investigación |
| `URL_PROYECCION` | URL del módulo de Proyección Social |
| `URL_CALIDAD` | URL del módulo de Calidad |

## Tecnologías

- **Backend:** Python 3 · Flask 3.1
- **Frontend:** Bootstrap 5.3 · Bootstrap Icons 1.11
- **Despliegue:** Railway · Gunicorn
- **Control de versiones:** GitHub — [chvn00/hub-teleco](https://github.com/chvn00/hub-teleco)
