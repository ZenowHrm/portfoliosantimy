from reactpy import component, html, use_state
from backend.crud_proyectos import *
from database import SessionLocal

from components.cards import Card, MCard
from components.modal import Modal

@component
def Home():
    tarjeta_activa, set_tarjeta_activa = use_state(None)

    def cerrar_modal():
        set_tarjeta_activa(None)
        
    card = get_card(SessionLocal(), 1)
    card2 = get_card(SessionLocal(), 2)
    card3 = get_card(SessionLocal(), 3)
    card4 = get_card(SessionLocal(), 4)
    home = html.div(
        {
            "style": {
                "display": "flex",
                "flex-direction": "column",
                "justify-content": "center",
                "align-items": "center",
            }
        },
        html.div(
            {
                "style": {
                    "display": "flex",
                    "flex-wrap": "wrap",
                    "justify-content": "center",
                }
            },
            Card(card, set_tarjeta_activa),
            Card(card2, set_tarjeta_activa),
            Card(card3, set_tarjeta_activa),
            Card(card4, set_tarjeta_activa),
        ),
        html.div(
            {
                "style": {
                    "display": "flex",
                    "flex-wrap": "wrap",
                    "justify-content": "center",
                    "max-width": "1000px",
                }
            },
            MCard(card2, set_tarjeta_activa),
            MCard(card3, set_tarjeta_activa),
            MCard(card, set_tarjeta_activa),
            MCard(card4, set_tarjeta_activa),
            MCard(card2, set_tarjeta_activa),
            MCard(card, set_tarjeta_activa),
        ),
        
        Modal(tarjeta_activa, cerrar_modal),
    )
    
    return home