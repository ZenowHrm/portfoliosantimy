from reactpy import component, html, event, use_state
from theme import COLORS

@component
def Modal(card_data, on_close):
    if not card_data:
        return html.div()
    
    boton_previa = html.a(
        {
            "href": card_data["previa"],
            "target": "_blank",
            "class_name": "btn-action btn-previa"
        }, 
        "Preview"
    ) if card_data["previa"] else None

    boton_descarga = html.a(
        {
            "href": card_data["descarga"],
            "target": "_blank",
            "class_name": "btn-action btn-descarga"
        }, 
        "Download"
    ) if card_data["descarga"] else None

    return html.div(
        {
            "class_name": "modal-overlay", 
            "on_click": lambda event: on_close(),
            "style": {
                "position": "fixed",
                "top": "0",
                "left": "0",
                "right": "0",
                "bottom": "0",
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
            /* --- ANIMACIONES Y EFECTOS --- */
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }

            @keyframes popIn {
                from { 
                    opacity: 0; 
                    transform: scale(0.95); /* Escala inicial sutil */
                }
                to { 
                    opacity: 1; 
                    transform: scale(1); 
                }
            }

            .modal-overlay {
                animation: fadeIn 0.25s ease-out forwards;
                /* Efecto de desenfoque extra para el fondo */
                backdrop-filter: blur(6px);
                -webkit-backdrop-filter: blur(6px); /* Soporte para Safari */
            }

            .modal-content-animated {
                /* Animación del contenido: suave y no exagerada */
                animation: popIn 0.3s ease-out forwards;
            }

            /* --- SCROLLBAR --- */
            .custom-scrollbar {
                /* Soporte para Firefox */
                scrollbar-width: thin;
                scrollbar-color: rgba(255, 255, 255, 0.2) transparent;
            }
            
            /* Soporte para Chrome, Edge, Safari */
            .custom-scrollbar::-webkit-scrollbar {
                width: 6px; 
            }
            
            .custom-scrollbar::-webkit-scrollbar-track {
                background: transparent; 
                margin: 10px 0; 
            }
            
            .custom-scrollbar::-webkit-scrollbar-thumb {
                background-color: rgba(255, 255, 255, 0.2); 
                border-radius: 10px; 
            }
            
            .custom-scrollbar::-webkit-scrollbar-thumb:hover {
                background-color: rgba(255, 255, 255, 0.4); 
            }

            /* --- ESTILOS DE LOS BOTONES --- */
            .btn-action {
                padding: 0.8rem 1.5rem;
                border-radius: 10px;
                font-weight: bold;
                text-decoration: none;
                text-align: center;
                transition: transform 0.2s, background 0.3s;
                font-size: 0.8rem;
                min-width: 120px;
            }
            .btn-previa {
                background: rgba(255, 255, 255, 0.15);
                color: white;
                border: 1px solid rgba(255, 255, 255, 0.3);
            }
            .btn-previa:hover {
                background: rgba(255, 255, 255, 0.3);
            }
            .btn-descarga {
                background: white;
                color: black;
            }
            .btn-descarga:hover {
                background: #f0f0f0;
                transform: scale(1.05); /* Efecto de crecimiento al pasar el cursor */
            }

            /* --- ADAPTACIÓN PARA MÓVIL --- */
            @media (max-width: 768px) {
                .modal-mobile {
                    width: 95% !important;
                    padding: 1.2rem !important;
                    max-height: 85vh !important; 
                    margin: auto !important; 
                }
                .botones-container {
                    /* En móviles, es mejor apilar los botones si son grandes */
                    flex-direction: column !important;
                    gap: 0.8rem !important;
                }
            }
            """
        ),
        html.div(
            {
                "on_click": event(lambda e: None, stop_propagation=True),
                "class_name": "custom-scrollbar modal-mobile modal-content-animated",
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
                    "margin": "auto", 
                    "color": "white"
                }
            },
            html.img({
                "src": card_data["img"], 
                "style": {"width": "100%", "border-radius": "15px", "margin-bottom": "1rem"}
            }),
            html.h2({"style": {"margin": "0 0 1rem 0"}}, card_data["titulo"]),
            html.p({"style": {"text-align": "center", "margin-bottom": "1.5rem"}}, card_data["descripcion"]),
            
            html.div(
                {
                    "class_name": "botones-container",
                    "style": {
                        "display": "flex", 
                        "gap": "1rem", 
                        "justify-content": "center", 
                        "width": "100%", 
                        "margin-top": "auto" 
                    }
                },
                *[b for b in [boton_previa, boton_descarga] if b is not None]
            )
        )
    )

@component
def EmailModal(on_close, on_verify, error_msg=""):
    code_input, set_code_input = use_state("")
    
    async def handle_submit(e):
        await on_verify(code_input)

    return html.div(
        {
            "class_name": "modal-overlay",
            "on_click": lambda event: on_close(),
            "style": {
                "position": "fixed",
                "top": "0",
                "left": "0",
                "right": "0",
                "bottom": "0",
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
            .btn-action {
                padding: 0.8rem 1.5rem;
                border-radius: 10px;
                font-weight: bold;
                text-decoration: none;
                text-align: center;
                transition: transform 0.2s, background 0.3s;
                font-size: 0.8rem;
                min-width: 120px;
            }
            .btn-descarga {
                background: white;
                color: black;
            }
            .btn-descarga:hover {
                background: #f0f0f0;
                transform: scale(1.05); 
            }
            """
        ),
        html.div(
            {
                "on_click": event(lambda e: None, stop_propagation=True), 
                "class_name": "modal-mobile modal-content-animated",
                "style": {
                    "box-sizing": "border-box",
                    "background": COLORS["degradado"],
                    "padding": "2.5rem 2rem",
                    "border-radius": "20px",
                    "width": "80%",
                    "max-width": "450px",
                    "box-shadow": "0px 10px 30px rgba(0,0,0,0.5)",
                    "display": "flex",
                    "flex-direction": "column",
                    "align-items": "center",
                    "margin": "auto", 
                    "color": "white"
                }
            },
            html.h2({"style": {"margin": "0 0 1rem 0", "text-align": "center", "font-size": "1.5rem"}}, "Verifica tu Identidad"),
            html.p(
                {"style": {"text-align": "center", "margin-bottom": "1.5rem", "font-size": "0.9rem"}}, 
                "Hemos enviado un código de 6 dígitos a tu correo. Ingrésalo a continuación."
            ),
            html.input({
                "type": "text",
                "placeholder": "123456",
                "max_length": "6",
                "value": code_input,
                "on_change": lambda e: set_code_input(e["target"]["value"]),
                "style": {
                    "width": "80%",
                    "padding": "12px 15px",
                    "background": "rgba(255, 255, 255, 0.05)",
                    "border": "1px solid #ff4444" if error_msg else "1px solid rgba(255, 255, 255, 0.3)",
                    "border-radius": "8px",
                    "color": "#ffffff",
                    "font-size": "1.5rem",
                    "text-align": "center",
                    "letter-spacing": "10px",
                    "margin-bottom": "5px",
                    "outline": "none"
                }
            }),
            html.p(
                {"style": {"color": "#ff4444", "font-size": "0.8rem", "margin-bottom": "15px", "min-height": "15px"}}, 
                error_msg 
            ),
            html.div(
                {"style": {"display": "flex", "gap": "1rem", "width": "100%", "justify-content": "center"}},
                html.button(
                    {
                        "on_click": lambda e: on_close(),
                        "class_name": "btn-action btn-previa", 
                        "style": {"cursor": "pointer"}
                    }, 
                    "Cancelar"
                ),
                html.button(
                    {
                        "on_click": handle_submit,
                        "disabled": len(code_input) < 6,
                        "class_name": "btn-action btn-descarga",
                        "style": {
                            "cursor": "pointer" if len(code_input) == 6 else "not-allowed", 
                            "opacity": "1" if len(code_input) == 6 else "0.5"
                        }
                    }, 
                    "Verificar"
                )
            )
        )
    )