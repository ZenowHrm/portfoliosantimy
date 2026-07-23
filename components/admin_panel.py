from reactpy import component, html, use_state, use_connection
from theme import COLORS, hex_to_rgba
from backend.auth import verificar_token

def extraer_cookie_segura(scope, nombre_cookie):
    headers = scope.get("headers", [])
    for key, value in headers:
        if key == b"cookie":
            cookies = value.decode("utf-8").split(";")
            for c in cookies:
                c = c.strip()
                if c.startswith(nombre_cookie + "="):
                    return c.split("=", 1)[1]
    return None

@component
def Adminpanel():
    conn = use_connection()
    contra_ingresada, set_contra_ingresada = use_state("")
    
    sesion = False
    token = extraer_cookie_segura(conn.scope, "access_token")
    if token:
        validacion = verificar_token(token)
        if validacion["valido"]:
            sesion = True
    
    def login_pag():
        esta_vacio = contra_ingresada == ""
        pag = html.div(
            {
                "style": {
                    "background": COLORS["degradado"],
                    "display": "flex",
                    "justifyContent": "center",
                    "alignItems": "center",
                    "minHeight": "100vh",
                    "fontFamily": "sans-serif"
                }
            },
            html.form(
                {
                    "method": "POST",
                    "action": "/api/login",
                    "style": {
                        "background": hex_to_rgba(COLORS["dark_bg"], 0.1),
                        "borderRadius": "16px",
                        "boxShadow": "0 4px 30px rgba(0, 0, 0, 0.1)",
                        "backdropFilter": "blur(8px)",
                        "-webkit-backdrop-filter": "blur(8px)",
                        "border": "1px solid rgba(215, 215, 215, 0.3)",
                        "padding": "40px",
                        "width": "300px",
                        "display": "flex",
                        "flexDirection": "column",
                        "gap": "15px"
                    }
                },
                html.p(
                    {
                        "style": {
                            "color": COLORS["light"],
                            "margin": "0",
                            "fontSize": "14px",
                            "textAlign": "left"
                        }
                    },
                    "Contraseña"
                ),
                html.input(
                    {
                        "type": "password",
                        "placeholder": "Coloque la contraseña",
                        "name": "contrasena",
                        "value": contra_ingresada,
                        "on_change": lambda e: set_contra_ingresada(e["target"]["value"]),
                        "style": {
                            "background": hex_to_rgba(COLORS["dark_bg"], 0.05),
                            "border": "1px solid rgba(215, 215, 215, 0.2)",
                            "borderRadius": "8px",
                            "padding": "12px",
                            "fontSize": "0.8rem",
                            "outline": "none",
                            "color": "white"
                        }
                    }
                ),
                html.button(
                    {
                        "type": "submit",
                        "disable": esta_vacio,
                        "style": {
                            "background": COLORS["primary"],
                            "color": COLORS["dark_bg"],
                            "border": "none",
                            "borderRadius": "8px",
                            "padding": "12px",
                            "fontSize": "0.8rem",
                            "fontWeight": "bold",
                            "cursor": "default",
                            "marginTop": "10px",
                            "opacity": "0.5" if esta_vacio else "1",
                            "pointer-events": "none" if esta_vacio else "auto"
                        }
                    },
                    "Iniciar Sesion"
                )
            ),
        )
        
        return pag
    
    def adminpanel_pag():
        pag = html.div(
            {
                
            },
            html.p(
                {
                    
                },
                "Sexo"
            )
            
        )
        
        return pag
    
    pag = html.div(
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
        login_pag() if not sesion else adminpanel_pag()
    )
    
    return pag