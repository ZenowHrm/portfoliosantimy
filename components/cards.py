from reactpy import component, html
from theme import COLORS, hex_to_rgba

ANIMATIONS_CSS = """
.animated-card {
    flex-shrink: 0;
    scroll-snap-align: center;
    z-index: 1; 
    transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    background: rgba(49, 49, 49, 0.65); 
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.5),
        inset 0 1px 0 rgba(255, 255, 255, 0.1),
        inset 0 -1px 0 rgba(0, 0, 0, 0.6), 
        inset 0 0 18px 9px rgba(0, 0, 0, 0.4); 
}
.animated-card:hover {
    transform: translateY(-4px);
}
.animated-card:active {
    transform: scale(0.97);
}

.animated-button {
    transition: transform 0.2s ease, filter 0.3s ease, box-shadow 0.3s ease;
}
.animated-card:hover .animated-button {
    filter: brightness(1.25);
    box-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
}
.animated-button:active {
    transform: scale(0.9);
}

@media (max-width: 657px) {
    .mcard {
        max-width: 1000px !important;
    }
}
"""

@component
def Card(card_data, on_card_click):
    card = html.div(
        {
            "loading": "lazy",
            "class_name": "animated-card",
            "on_click": lambda event: on_card_click({
                "img": card_data.url_imagen, 
                "titulo": card_data.titulo, 
                "descripcion": card_data.descripcion_larga,
                "descarga": card_data.url_descarga,
                "previa": card_data.url_previa
            }),
            "style": {
                "cursor": "pointer",
                "overflow": "hidden",
                "display": "flex",
                "flex-direction": "column",
                "width": "clamp(150px, 30vw, 12rem)", 
                "height": "clamp(180px, 40vw, 230px)",
                "border-radius": "clamp(15px, 4vw, 30px)",
                "font-size": "clamp(0.5rem, 1.5vw, 0.6rem)",
            }
        },
        html.style(ANIMATIONS_CSS), 
        html.div(
            {
                "class_name": "img_container",
                "style": {
                    "width": "100%",
                    "height": "45%", 
                    "flex-shrink": "0"
                }
            },
            html.img(
                {
                    "src": f"{card_data.url_imagen}?w=200",
                    "style": {
                        "width": "100%",
                        "height": "100%",
                        "object-fit": "cover" 
                    }
                }
            )
        ),
        html.div(
            {
                "style": {
                    "flex": "1",
                    "overflow": "hidden",
                    "display": "flex",
                    "flex-direction": "column",
                    "justify-content": "center",
                    "text-align": "left",
                    "margin": "clamp(0.3rem, 1.5vw, 1rem)",
                    "gap": "clamp(3px, 1vw, 10px)"
                }
            },
            html.h3(
                {
                    "style": {
                        "margin": "0",
                        "font-size": "clamp(0.66rem, 2.5vw, 1.1em)",
                        "white-space": "nowrap",
                        "overflow": "hidden",
                        "text-overflow": "ellipsis"
                    }
                },
                f"{card_data.titulo}"
            ),
            html.p(
                {
                    "style": {
                        "color": f"{hex_to_rgba(COLORS["light"], 0.9)}",
                        "margin": "0",
                        "display": "-webkit-box",
                        "-webkit-box-orient": "vertical",
                        "overflow": "hidden"
                    }
                },
                f"{card_data.descripcion_corta}"
            )
        ),
        html.div(
            {
                "style": {
                    "display": "flex",
                    "justify-content": "flex-end",
                    "width": "100%",
                    "margin-top": "auto"
                }
            },
            html.div(
                {
                    "class_name": "animated-button", 
                    "style": {
                        "display": "flex",
                        "flex-direction": "row", 
                        "justify-content": "center",
                        "align-items": "center",
                        "background": COLORS["dark_bg"],
                        "width": "fit-content",
                        "border": "1px solid rgba(255, 255, 255, 0.08)",
                        "border-radius": "4px",
                        "padding": "clamp(0.2em, 1vw, 0.5em) clamp(0.5em, 2vw, 2em)",
                        "margin": "0 clamp(0.5rem, 2vw, 1rem) clamp(0.5rem, 2vw, 1rem) 0",
                    }
                },
                html.i({"class_name": "material-icons", "style": {"font-size": "0.5rem"}}, "arrow_forward"),
                html.p(
                    {
                        "style": {
                            "margin": "0 0 0 5px", 
                            "font-size": "inherit",
                        }
                    },
                    "More"
                )
            )
        )
    )
    
    return card

@component
def MCard(card_data, on_card_click):
    card = html.div(
        {
            "loading": "lazy",
            "class_name": "animated-card mcard", 
            "on_click": lambda event: on_card_click({
                "img": card_data.url_imagen, 
                "titulo": card_data.titulo, 
                "descripcion": card_data.descripcion_larga,
                "descarga": card_data.url_descarga,
                "previa": card_data.url_previa
            }),
            "style": {
                "display": "flex",
                "flex-direction": "row",
                "align-items": "stretch",
                "cursor": "pointer",
                "overflow": "hidden",
                "width": "calc(100% - 2rem)",
                "max-width": "300px",
                "max-height": "87px",
                "border-radius": "10px",
            }
        },
        html.style(ANIMATIONS_CSS), 
        html.div(
            {
                "class_name": "img_container",
                "style": {
                    "flex": "0 0 30%",
                    "min-height": "50px", 
                }
            },
            html.img(
                {
                    "src": f"{card_data.url_imagen}?w=100",
                    "style": {
                        "width": "100%",
                        "height": "100%",
                        "object-fit": "cover",
                        "object-position": "center",
                    }
                }
            )
        ),
        html.div(
            {
                "style": {
                    "display": "flex",
                    "flex-direction": "column",
                    "justify-content": "center",
                    "padding": "1rem", 
                    "gap": "5px",
                    "overflow": "hidden"
                }
            },
            html.h3(
                {
                    "style": {
                        "word-break": "break-word",
                        "overflow-wrap": "break-word",
                        "margin": "0", 
                        "font-size": "0.6rem",
                        "white-space": "nowrap", 
                        "text-overflow": "ellipsis", 
                        "overflow": "hidden"
                    }
                },
                f"{card_data.titulo}"
            ),
            html.p(
                {
                    "style": {
                        "word-break": "break-word",
                        "overflow-wrap": "break-word",
                        "margin": "0", 
                        "font-size": "0.5rem",
                        "opacity": "0.9"
                    }
                },
                f"{card_data.descripcion_corta}"
            )
        ),
        html.div(
            {
                "style": {
                    "flex": "0 0 auto",
                    "display": "flex",
                    "align-items": "center",
                    "padding": "0 1rem 0 0",
                }
            },
            html.div(
                {
                    "class_name": "animated-button", 
                    "style": {
                        "display": "flex",
                        "justify-content": "center",
                        "align-items": "center",
                        "background": COLORS["dark_bg"],
                        "width": "28px",
                        "height": "28px",
                        "border": "1px solid rgba(255, 255, 255, 0.08)",
                        "border-radius": "50%", 
                    }
                },
                html.i({"class_name": "material-icons","style": {"font-size": "1rem"}},"arrow_forward")
            )
        )
    )
    
    return card