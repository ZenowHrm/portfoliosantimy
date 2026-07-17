from reactpy import component, html
from theme import COLORS

@component
def Menu(view, set_view):
    def crear_boton(id, texto):
        if view == id:
            stylo = {
                "background": COLORS["medium_blue"], 
                "box-shadow": "0 0 12px rgba(0, 212, 255, 0.8)",
                "border": "1px solid transparent"
            }
            if id == "yo":
                stylo = {
                    "background": COLORS["medium_blue"],
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
                    "background": "rgba(4, 4, 4, 0.65)",
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

    menu = html.div(
        {
            "class_name": "menu-wrapper"
        },
        html.style(
            """
                .menu-wrapper {
                    display: flex;
                    flex-direction: row;
                    width: 100%;
                    justify-content: center;
                }

                button {
                    background: none;          
                    border: 1px solid transparent;                
                    padding: 10px 20px;                
                    margin: 0;                
                    cursor: pointer;          
                    font: inherit;            
                    color: inherit;            
                    outline: none;
                    font-size: 0.8rem;
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
                    
                    /* --- EFECTO DARK GLASSMORPHISM --- */
                    background: rgba(4, 4, 4, 0.65);
                    backdrop-filter: blur(20px);
                    -webkit-backdrop-filter: blur(20px);
                    border: 1px solid rgba(255, 255, 255, 0.08);
                    box-shadow: 
                        0 8px 32px rgba(0, 0, 0, 0.5),
                        inset 0 1px 0 rgba(255, 255, 255, 0.1),
                        inset 0 -1px 0 rgba(0, 0, 0, 0.6), 
                        inset 0 0 18px 9px rgba(0, 0, 0, 0.4); 
                    /* --------------------------------- */

                    bottom: 1.5rem;
                    left: 0;
                    width: 100%;
                    height: 50%;
                    z-index: -1;
                    border-radius: 999px;
                }
                
                .btn-yo {
                    background: none;
                    border-radius: 50%;
                    width: 4.7rem;
                    height: 4.5rem;
                    padding: 0;
                    margin: 0;
                }
                
                .material-icons {
                    font-size: 3.5rem;
                }
                
                @media (max-width: 657px) {
                    .menu-wrapper {
                        justify-content: flex-start;
                        padding: 0;
                    }
                    .btn-yo {
                        order: -1; 
                        width: 3.2rem;
                        height: 3rem;
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
                
                crear_boton("yo", i),
                
                crear_boton("ideas", "Ideas"),
                crear_boton("logs", "Logs"),
            ),
        ),
        
    )
    
    return menu