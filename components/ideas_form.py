from reactpy import component, html
from theme import COLORS

@component
def Ideas():
    ideas = html.div(
        {
            "style": {
            }
        },
        html.style(
            """
                @media (max-width: 657px) {
                    .texto {
                        font-size: 0.8rem !important;
                    } 
                }
            """
        ),
        html.div(
            {
                "style": {
                    "box-sizing": "border-box",
                    "background": COLORS["dark_bg"],
                    "padding": "1rem",
                    "border-radius": "20px",
                    "width": "80%",
                    "max-width": "600px",
                    "box-shadow": "0px 10px 30px rgba(0,0,0,0.5)",
                    "display": "flex",
                    "flex-direction": "column",
                    "align-items": "center",
                    "margin": "auto", 
                }
            },
            html.h3(
                {
                    "style": {
                        "text-align": "center",
                    }
                },
                "Do you have any ideas or projects in mind?"
            ),
            html.p(
                {
                    "style": {
                        "text-align": "center",
                        "font-size": "0.8rem",
                        "padding": "10px 0 0 0"
                    }
                },
                "Si tienes alguna idea que quieras compartir, escríbela aquí. También puedes usar este espacio para contactarme si te interesa que colaboremos y desarrollemos algún proyecto juntos."
            ),
            html.div(
                {
                    "style": {
                        "display": "flex",
                        "flex-direction": "column",
                        "padding": "20px",
                    }
                },
                html.p(
                    {
                        
                    },
                    "Usuario"
                ),
                html.input(
                    {
                        "type": "text",
                        "placeholder": "Nombre de Usuario",
                        "value": "",
                        "on_change": "",
                        "style": {
                            "width": "100%",
                            "padding": "12px 15px",
                            "background": "rgba(255, 255, 255, 0.05)",  
                            "border": "1px solid rgba(255, 255, 255, 0.2)",
                            "border-radius": "8px",
                            "color": "#ffffff", 
                            "font-size": "0.8rem",
                            "box-sizing": "border-box",
                            "outline": "none"
                        }
                    }
                ),
                html.p(
                    {
                        "style": {
                            "margin": "10px 0 0 0"
                        }
                    },
                    "Idea / Consulta"
                ),
                html.textarea(
                    {
                        "placeholder": "Escribe aquí",
                        "value": "",
                        "on_change": "",
                        "style": {
                            "width": "100%",
                            "padding": "12px 15px",
                            "background": "rgba(255, 255, 255, 0.05)",  
                            "border": "1px solid rgba(255, 255, 255, 0.2)",
                            "border-radius": "8px",
                            "color": "#ffffff", 
                            "font-size": "0.8rem",
                            "box-sizing": "border-box",
                            "outline": "none",
                            "min-height": "150px",  # Lo hace un poco más grande
                            "resize": "none",       # Quita la opción de redimensionar
                            "font-family": "inherit", # Mantiene la fuente consistente
                            "margin": "0 0 10px 0",
                        }
                    }
                ),
                html.div(
                    {
                        "style": {
                            "box-sizing": "border-box",
                            "background": COLORS["medium_gray"],
                            "padding": "1rem",
                            "border-radius": "20px",
                            "width": "100%",
                            "box-shadow": "0px 10px 30px rgba(0,0,0,0.5)",
                            "margin": "auto", 
                        }
                    },
                    html.p(
                        {
                            "class-name": "texto",
                        },
                        "Por motivos de seguridad, Ingresa tu correo electronico para una verificación"
                    )
                ),
                html.p(
                    {
                        "style": {
                            "margin": "10px 0 0 0"
                        }
                    },
                    "Correo"
                ),
                html.input(
                    {
                        "type": "email",
                        "placeholder": "example@gmail.com",
                        "value": "",
                        "on_change": "",
                        "style": {
                            "width": "100%",
                            "padding": "12px 15px",
                            "background": "rgba(255, 255, 255, 0.05)",  
                            "border": "1px solid rgba(255, 255, 255, 0.2)",
                            "border-radius": "8px",
                            "color": "#ffffff", 
                            "font-size": "0.8rem",
                            "box-sizing": "border-box",
                            "outline": "none"
                        }
                    }
                )
            ),
            html.button(
                {
                    "style": {
                        "display": "flex",
                        "font-size": "1rem",
                        "flex-direction": "row", 
                        "justify-content": "center",
                        "align-items": "center",
                        "background": COLORS["dark_bg"],
                        "width": "250px",
                        "border": "1px solid rgba(255, 255, 255, 0.08)",
                        "border-radius": "4px",
                        "padding": "clamp(0.2em, 1vw, 0.5em) clamp(0.5em, 2vw, 2em)",
                    }
                },
                "Send"
            )
        )
    )
    
    return ideas