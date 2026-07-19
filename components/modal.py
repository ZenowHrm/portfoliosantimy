from reactpy import component, html, event
from theme import COLORS

@component
def Modal(card_data, on_close):
    if not card_data:
        return html.div()
        
    return html.div(
        {
            "on_click": lambda event: on_close(),
            "style": {
                "position": "fixed",
                "top": "0",
                "left": "0",
                "width": "100vw",
                "height": "100vh",
                "background-color": "rgba(0, 0, 0, 0.7)", 
                "display": "flex",
                "justify-content": "center",
                "font-size": "0.6rem",
                "align-items": "center",
                "z-index": "1000", 
            }
        },
        html.style(
            """
            .custom-scrollbar {
                /* Soporte para Firefox */
                scrollbar-width: thin;
                scrollbar-color: rgba(255, 255, 255, 0.2) transparent;
            }
            
            /* Soporte para Chrome, Edge, Safari */
            .custom-scrollbar::-webkit-scrollbar {
                width: 6px; /* Barra delgada y minimalista */
            }
            
            .custom-scrollbar::-webkit-scrollbar-track {
                background: transparent; /* El riel es invisible para no tapar tu degradado */
                margin: 10px 0; /* Un poco de margen para que no toque los bordes superior/inferior */
            }
            
            .custom-scrollbar::-webkit-scrollbar-thumb {
                background-color: rgba(255, 255, 255, 0.2); /* Gris/blanco muy sutil */
                border-radius: 10px; /* Bordes redondeados */
            }
            
            .custom-scrollbar::-webkit-scrollbar-thumb:hover {
                background-color: rgba(255, 255, 255, 0.4); /* Se ilumina ligeramente al pasar el mouse */
            }
            """
        ),
        html.div(
            {
                "on_click": event(lambda e: None, stop_propagation=True),
                "class_name": "custom-scrollbar",
                "style": {
                    "box-sizing": "border-box",
                    "max-height": "90vh",
                    "overflow-y": "auto",
                    "background": COLORS["degradado"],
                    "padding": "2rem",
                    "border-radius": "20px",
                    "width": "80%",
                    "max-width": "700px",
                    "box-shadow": "0px 10px 30px rgba(0,0,0,0.5)",
                    "display": "flex",
                    "flex-direction": "column",
                    "align-items": "center",
                    "color": "white"
                }
            },
            html.img({
                "src": card_data["img"], 
                "style": {"width": "100%", "border-radius": "15px", "margin-bottom": "1rem"}
            }),
            html.h2({"style": {"margin": "0 0 1rem 0"}}, card_data["titulo"]),
            html.p({"style": {"text-align": "center", "margin-bottom": "1.5rem"}}, card_data["descripcion"]),
        )
    )