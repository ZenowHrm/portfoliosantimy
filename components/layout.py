from reactpy import component, html
from theme import COLORS

@component
def Menu(view, set_view):
    def crear_boton(id, texto):
        if view == id:
            stylo = {
                "background": COLORS["medium_gray"], 
                "box-shadow": f"0 0 12px {COLORS["deep_gray"]}",
                "border": "1px solid transparent"
            }
            if id == "yo":
                stylo = {
                    "background": COLORS["medium_gray"],
                    "box-shadow": "0 0 12px rgba(0, 212, 255, 0.8)",
                    "border": "1px solid rgba(255, 255, 255, 0.15)",
                }
        else:
            stylo = {
                "background": "transparent", 
                "box-shadow": "none",
                "border": "1px solid transparent"
            }
            if id == "yo":
                stylo = {
                    "background": COLORS["dark_bg"],
                    "backdrop-filter": "blur(20px)",
                    "-webkit-backdrop-filter": "blur(20px)",
                    "border": "1px solid rgba(255, 255, 255, 0.08)",
                    "box-shadow": "0 8px 32px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.1), inset 0 -1px 0 rgba(0, 0, 0, 0.6), inset 0 0 18px 9px rgba(0, 0, 0, 0.4)"
                }
        
        return html.button(
                {
                    "on_click": lambda event: set_view(id),
                    "style": stylo,
                    "class_name": f"btn-{id}"
                }, 
                texto,
            )
    
    i = html.i({"class_name": "material-icons", "style": {}}, "visibility")

    menu =  html.div(
                {
                    "style": {
                        "z-index": "999", 
                        "position": "sticky",
                        "left": "0",
                        "top": "0",
                        "width": "100%",
                    }
                },
                html.div(
                    {
                        "class_name": "menu-wrapper",
                        "style": {}
                    },
                    html.style(
                        """
                            .menu-wrapper {
                                display: flex;
                                flex-direction: row;
                                justify-content: center;
                                position: relative;    
                            }

                            button {
                                background: none;          
                                border: 1px solid transparent;                
                                padding: 8px 15px;                
                                margin: 0;                
                                cursor: pointer;          
                                font: inherit;            
                                color: inherit;            
                                outline: none;
                                font-size: 0.7rem;
                                font-weight: 600;
                                border-radius: 999px;
                                transition: background 0.3s ease, box-shadow 0.3s ease, transform 0.2s ease, border 0.3s ease, backdrop-filter 0.3s ease;
                            }
                            button:hover {
                                transform: scale(1.05);
                            }
                            button:active {
                                transform: scale(0.95);
                            }
                            .menuContainer::before {
                                content: "";
                                position: absolute;
                                
                                background: rgba(49, 49, 49, 0.65); 
                                backdrop-filter: blur(20px);
                                -webkit-backdrop-filter: blur(20px);
                                border: 1px solid rgba(255, 255, 255, 0.08);
                                box-shadow: 
                                    0 8px 32px rgba(0, 0, 0, 0.5),
                                    inset 0 1px 0 rgba(255, 255, 255, 0.1),
                                    inset 0 -1px 0 rgba(0, 0, 0, 0.6), 
                                    inset 0 0 18px 9px rgba(0, 0, 0, 0.4);

                                bottom: 1.4rem;
                                left: 0;
                                width: 100%;
                                height: 50%;
                                z-index: -1;
                                border-radius: 999px;
                            }
                            
                            .btn-yo {
                                background: none;
                                border-radius: 50%;
                                width: 4.2rem;
                                height: 4rem;
                                padding: 0;
                                margin: 0;
                            }
                            
                            .material-icons {
                                font-size: 3rem;
                            }
                            
                            .menuContainer button:not(.btn-yo) {
                                min-width: 6.5rem; 
                                text-align: center;
                            }
                            
                            .yo-wrapper {
                                position: relative;
                                isolation: isolate;
                                display: flex;
                                flex-direction: column;
                                align-items: center;
                            }
                            
                            .yo-tooltip {
                                position: absolute;
                                bottom: -2rem;
                                background: #313131;
                                border: 1px solid rgba(255, 255, 255, 0.15);
                                border-radius: 6px;
                                color: white;
                                font-size: 0.65rem;
                                font-weight: 600;
                                padding: 4px 10px;
                                white-space: nowrap;
                                box-shadow: 0 6px 14px rgba(0, 0, 0, 0.4);
                                pointer-events: none; 
                                z-index: 10;
                                
                                opacity: 0;
                                visibility: hidden;
                                transform: translateY(-5px); 
                                transition: opacity 0.3s ease, transform 0.3s ease, visibility 0.3s ease;
                            }
                            .yo-tooltip::after {
                                content: '';
                                position: absolute;
                                top: -4px;
                                left: 50%;
                                transform: translateX(-50%) rotate(45deg);
                                width: 8px;
                                height: 8px;
                                background: #313131;
                                border-top: 1px solid rgba(255, 255, 255, 0.15);
                                border-left: 1px solid rgba(255, 255, 255, 0.15);
                            }

                            .yo-wrapper:hover .yo-tooltip {
                                opacity: 1;
                                visibility: visible;
                                transform: translateY(0); /* Baja a su posición natural */
                            }
                            /* -------------------------------------- */
                            
                            @media (max-width: 657px) {
                                .menu-wrapper {
                                    justify-content: flex-start;
                                    padding: 0;
                                }
                                .btn-yo {
                                    width: 3.2rem;
                                    height: 3rem;
                                }
                                .yo-wrapper{
                                    order: -1;
                                }
                                .material-icons {
                                    font-size: 2rem;
                                }
                                button {
                                    font-size: 0.6rem;
                                    padding: 5px 10px;
                                    
                                }
                                .menuContainer {
                                    margin: 1rem 10px !important;
                                }
                                .menuContainer::before {
                                    bottom: 1.3rem;
                                    left: 1.5rem;
                                    width: 90%;
                                    height: 45%;
                                }
                                .menuContainer button:not(.btn-yo) {
                                    min-width: auto;
                                }
                                .yo-tooltip {
                                    font-size: 0.55rem;
                                    opacity: 0 !important;
                                    visibility: hidden !important;
                                }
                            }
                        """
                    ),
                    html.div(
                        {
                            "style": {
                                "position": "relative",
                                "isolation": "isolate",
                                "padding": "0",
                                "margin": "0",
                            },
                        },
                        html.div(
                            {
                                "class_name": "menuContainer",
                                "style": {
                                    "display": "flex",
                                    "flex-direction": "row",
                                    "align-items": "center",
                                    "justify-content": "center",
                                    "gap": "5px",
                                    "margin": "1rem" ,
                                },
                            },
                            
                            crear_boton("home", "Home"),
                            crear_boton("projects", "Projects"),
                            
                            html.div(
                                {"class_name": "yo-wrapper"},
                                crear_boton("yo", i),
                                html.span(
                                    {"class_name": "yo-tooltip"}, 
                                    "About Me"
                                )
                            ),
                            
                            crear_boton("ideas", "Ideas"),
                            crear_boton("logs", "Logs"),
                        ),
                    ),
                    
                )
    )
    
    return menu