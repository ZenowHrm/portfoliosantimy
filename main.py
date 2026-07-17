from fastapi import FastAPI
from reactpy import component, html, use_state
from reactpy.backend.fastapi import configure

from theme import COLORS

from components.layout import Menu
from components.home import Home
from components.gallery import Projects
from components.me import Me
from components.ideas_form import Ideas
from components.logs_view import Logs


app = FastAPI()
app.add_websocket_route = app.add_api_websocket_route
# ---------------------------------------

@component
def App():
    view, set_view = use_state("home")
    
    def set_pag(vista):
        pag = Home()
        if vista == "home":
            pag = Home()
        elif vista == "projects":
            pag = Projects()
        elif vista == "yo":
            pag = Me()
        elif vista == "ideas":
            pag = Ideas()
        elif vista == "logs":
            pag = Logs()
        return pag
    
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
        html.head(
            html.link({
                "rel": "stylesheet",
                "href": "https://fonts.googleapis.com/icon?family=Material+Icons"
            }),
            html.link({
                "rel": "stylesheet",
                "href": "https://fonts.googleapis.com/css2?family=Sono:wght@200..800&display=swap"
            })
        ),
        html.meta({"name": "viewport", "content": "width=device-width, initial-scale=1.0"}),
        html.style(
            """
                * {
                    margin: 0;
                    padding: 0;
                    color: #ffffff;
                    font-family: Sono, sans-serif;
                }
            """),
        html.div(
            {
                "style": {
                    "position": "sticky",
                    "right": "0",
                    "top": "0",
                }
            },Menu(view, set_view),
            
        ),
        set_pag(view)
    )
    
    return pagina

configure(app, App)