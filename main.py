import os
from dotenv import load_dotenv
from fastapi import FastAPI, Form
from reactpy import component, html, use_state
from reactpy.backend.fastapi import configure, Options
from reactpy_router import browser_router, route
from fastapi.staticfiles import StaticFiles
from database import engine
from backend.auth import verificar_contrasena, crear_token_acceso
from fastapi.responses import RedirectResponse

import models

from theme import COLORS

from components.layout import Menu
from components.home import Home
from components.gallery import Projects
from components.me import Me
from components.ideas_form import Ideas
from components.logs_view import Logs
from components.admin_panel import Adminpanel

load_dotenv()

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_websocket_route = app.add_api_websocket_route
app.mount("/static", StaticFiles(directory="static"), name="static")

MINUTOS_DE_SESION = 60
entorno = ("produccion" == os.getenv("ENTORNO"))
# ---------------------------------------

opciones_reactpy = Options(
    head=html.head(
        html.title("Portfolio SantiMY"),
        html.meta({"name": "viewport", "content": "width=device-width, initial-scale=1.0"}),
        html.link({"rel": "icon", "type": "image/png", "href": "/static/img/perfil.png"}),
        html.link({"rel": "stylesheet", "href": "https://fonts.googleapis.com/icon?family=Material+Icons"}),
        html.link({"rel": "stylesheet", "href": "https://fonts.googleapis.com/css2?family=Sono:wght@200..800&display=swap"}),
        html.style(
            """
                * {
                    margin: 0;
                    padding: 0;
                    color: #ffffff;
                    font-family: 'Sono', sans-serif;
                    box-sizing: border-box;
                }
                input[type="password"]::-ms-reveal {
                    filter: invert(1);
                }
            """
        )
    )
)

@component
def Aplicacion():
    view, set_view = use_state("home")
    
    def set_pag():
        if view == "projects":
            return Projects()
        elif view == "yo":
            return Me()
        elif view == "ideas":
            return Ideas()
        elif view == "logs":
            return Logs()
        return Home()
    
    pagina = html.div(
        {
            "style": {
                "background": COLORS["degradado"],
                "width": "100%",
                "min-height": "100vh",        
                "margin": "0",
                "padding": "0",
                "box-sizing": "border-box",
                }
        },
        Menu(view, set_view),
        set_pag(),
    )
    
    return pagina

@component
def App():
    return browser_router(
        route("/", Aplicacion()),
        route("/auth_process37", Adminpanel())
    )

@app.post("/api/login")
def login(contrasena: str = Form(...)):
    if verificar_contrasena(contrasena):
        
        token = crear_token_acceso({"usuario": "admin"}, MINUTOS_DE_SESION)
        
        respuesta = RedirectResponse(url="/auth_process37", status_code=303)
        
        respuesta.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            secure=entorno,
            samesite="lax",
            max_age=MINUTOS_DE_SESION * 60
        )
        return respuesta

    return RedirectResponse(url="/auth_process37?error=1", status_code=303)

configure(app, App, options=opciones_reactpy)