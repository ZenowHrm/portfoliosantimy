from reactpy import component, html, use_state
from backend.crud_proyectos import *
from database import SessionLocal
from theme import COLORS

from components.cards import Card
from components.modal import Modal

@component
def Projects():
    tarjeta_activa, set_tarjeta_activa = use_state(None)
    index, set_index = use_state(0)
    verify, set_verify = use_state(True)
    
    def mover_derecha(event):
        if verify:
            set_index(index + 1)
            
    def mover_izquierda(event):
        if index > 0:
            set_index(index - 1)
    
    def proyectos():
        db = SessionLocal()
        try:
            lista = get_cards(db, (index * 10), 10)
            card = ()
            for i in lista:
                card = card + (Card(i, set_tarjeta_activa),)
            if card == ():
                set_verify(False)
                return html.div(
                            {
                                "style": {
                                    "width": "100%",
                                    "height": "65.5dvh",
                                    "display": "flex",
                                    "align-items": "center",
                                    "justify-content": "center",
                                }
                            },
                            html.p(
                                {
                                    "style": {
                                        "font-size": "1.5rem",
                                    }
                                },
                                "That's all for now."
                            )
                        )
            else:
                set_verify(True)
                return card
        finally:
            db.close()
    
    def cerrar_modal():
        set_tarjeta_activa(None)
        
    STYLE_BUTTON = {
        "display": "flex",
        "flex-direction": "row", 
        "justify-content": "center",
        "align-items": "center",
        "background": COLORS["dark_bg"],
        "width": "fit-content",
        "border": "1px solid rgba(255, 255, 255, 0.08)",
        "border-radius": "4px",
        "padding": "clamp(0.2em, 1vw, 0.5em) clamp(0.5em, 2vw, 2em)",
    }
    
    projects = projects = html.div(
        {
            "style": {
                "width": "100%",
                "height": "100%",
                "display": "flex",
                "flex-direction": "column",
                "align-items": "center",
                "box-sizing": "border-box"
            }
        },
        # --- CONTENEDOR DE TARJETAS ---
        html.div(
            {
                "style": {
                    "display": "flex",
                    "flex-wrap": "wrap",
                    "gap": "20px",
                    "max-width": "1100px",
                    "width": "100%",
                    "justify-content": "center",  
                    "align-content": "center",    
                    "flex": "1",                 
                    "overflow-y": "auto",         
                    "padding": "20px",
                    "box-sizing": "border-box"
                }
            },
            proyectos()
        ),
        html.div(
            {
                "style": {
                    "display": "flex",
                    "justify-content": "center",
                    "align-items": "center",
                    "gap": "30px",           
                    "padding": "15px 20px",
                    "width": "100%",
                    "position": "sticky",       
                    "bottom": "0",              
                    "box-shadow": "0px -4px 10px rgba(0,0,0,0.05)",
                    "z-index": "10"
                }
            },
            html.button(
                {
                    "on_click": mover_izquierda,
                    "style": STYLE_BUTTON
                },
                "Izquierda"
            ),
            html.span(
                {
                    "style": {
                        "margin": "0",
                        "font-size": "1rem",
                        "text-align": "center"
                    }
                },
                f"{index+1}"
            ),
            html.button(
                {
                    "on_click": mover_derecha,
                    "style": STYLE_BUTTON
                },
                "Derecha"
            )
        ),
        Modal(tarjeta_activa, cerrar_modal)
    )
    
    return projects