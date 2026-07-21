from fastapi import FastAPI
from reactpy import component, html, use_state
from reactpy.backend.fastapi import configure, Options
from reactpy_router import browser_router, route, link
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import SessionLocal, engine

import models

from theme import COLORS

from components.layout import Menu
from components.home import Home
from components.gallery import Projects
from components.me import Me
from components.ideas_form import Ideas
from components.logs_view import Logs
from components.admin_panel import Adminpanel

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_websocket_route = app.add_api_websocket_route
app.mount("/static", StaticFiles(directory="static"), name="static")
# ---------------------------------------

opciones_reactpy = Options(
    head=html.head(
        html.meta({"name": "viewport", "content": "width=device-width, initial-scale=1.0"}),
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
        route("/admin", Adminpanel())
    )

configure(app, App, options=opciones_reactpy)