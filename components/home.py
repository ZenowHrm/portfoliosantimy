from reactpy import component, html, use_state
from backend.crud_proyectos import *

from components.cards import Card, MCard
from components.modal import Modal

@component
def Home():
    tarjeta_activa, set_tarjeta_activa = use_state(None)
    
    def destacadas():
        lista = get_destacadas(5)
        card = ()
        for i in lista:
            card = card + (Card(i, set_tarjeta_activa),)
        return card
    
    def recientes():
        lista = get_recientes(6)
        card = ()
        for i in lista:
            card = card + (MCard(i, set_tarjeta_activa),)
        return card

    
    def cerrar_modal():
        set_tarjeta_activa(None)

    home = html.div(
        {
            "style": {
            }
        },
        html.style(
            """
            .Destacados {
                /* Soporte para Firefox */
                scrollbar-width: thin;
                scrollbar-color: rgba(255, 255, 255, 0.2) transparent;
            }
            
            /* Soporte para Chrome, Edge, Safari */
            .Destacados::-webkit-scrollbar {
                width: 6px; 
            }
            
            .Destacados::-webkit-scrollbar-track {
                background: transparent; 
                margin: 10px 0; 
            }
            
            .Destacados::-webkit-scrollbar-thumb {
                background-color: rgba(255, 255, 255, 0.2); 
                border-radius: 10px; 
            }
            
            .Destacados::-webkit-scrollbar-thumb:hover {
                background-color: rgba(255, 255, 255, 0.4); 
            }
            
            @media (max-width: 1000px) {
                .Destacados {
                    justify-content: flex-start !important;
                }
            }
            """
        ),
        html.div(
            {
                "class-name": "perfil",
                "style": {
                    "font-size": "0.7rem",
                    "width": "100%",
                    "display": "flex",
                    "flex-direction": "column",
                    "align-items": "center",
                    "justify-content": "center", 
                }
            },
            html.div(
                {
                    "class-name": "imgperfil-container",
                    "style": {
                        "width": "100px",
                        "height": "100px",
                        "border-radius": "50%",
                        "overflow": "hidden",
                    }
                },
                html.img(
                    {
                        "src": "/static/img/perfil.png",
                        "style": {
                            "width": "100%"
                        }
                    }
                )
            ),
            html.h1(
                {},
                "Santiago Maya"
            ),
            html.p(
                {},
                "Fullstack Programmer and Video Game Developer"
            )
        ),
        
        html.div(
            {
                "style": {
                    "width": "100%",
                    "display": "flex",
                    "flex-direction": "column",
                    "align-items": "center",
                }
            },
            html.div(
                {
                    "style": {
                        "width": "100%",
                        "max-width": "1050px",
                    }
                },
                html.h5(
                    {
                        "style": {
                            "padding": "12px 0 0 12px",
                            "margin": "0",
                        }
                    },
                    "Featured projects"
                ),
            ),
            html.div(
                {
                    "class_name": "Destacados",
                    "style": {
                        "width": "100%",
                        "display": "flex",
                        "max-width": "1050px",
                        "overflow-x": "auto",
                        "gap": "16px",
                        "padding": "12px",
                        "scroll-snap-type": "x mandatory",
                    }
                },
                destacadas(),
            )
        ),
        
        html.div(
            {
                "style": {
                    "width": "100%",
                    "display": "flex",
                    "flex-direction": "column",
                    "align-items": "center",
                }
            },
            html.div(
                {
                    "style": {
                        "width": "100%",
                        "max-width": "950px",
                    }
                },
                html.h5(
                    {
                        "style": {
                            "padding": "12px 0 0 12px",
                            "margin": "0",
                        }
                    },
                    "Recently"
                ),
            ),
            html.div(
                {
                    "style": {
                        "display": "flex",
                        "padding": "12px 0 0 0",
                        "flex-wrap": "wrap",
                        "gap": "10px",
                        "max-width": "940px",
                        "justify-content": "center", 
                    }
                },
                recientes()
            )
        ),
        
        Modal(tarjeta_activa, cerrar_modal)
    )
    
    return home