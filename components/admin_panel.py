from reactpy import component, html, use_state, use_connection, event
from theme import COLORS, hex_to_rgba
from backend.auth import verificar_token
from database import SessionLocal
from backend.crud_proyectos import *
from backend import schemas


BUTTONS_STYLE = {
    "background": COLORS["primary"],
    "color": COLORS["dark_bg"],
    "border": "none",
    "borderRadius": "8px",
    "padding": "12px",
    "fontSize": "0.8rem",
    "fontWeight": "bold",
    "cursor": "default",
    "width": "100%"
}

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
                            **BUTTONS_STYLE,
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
        opcion_seleccionada, set_opcion_seleccionada = use_state(None)
        activo_m, set_activo = use_state(False)
        type_process, set_type_process = use_state("")
        
        def abrir_modal(type_bt):
            set_activo(True)
            set_type_process(type_bt)
        
        def cerrar_modal():
            set_activo(False)
        
        def proyectos():
            db = SessionLocal()
            try:
                lista = get_cards(db, 0, 100)
                card = ()
                for i in lista:
                    card = card + (cards_elements(i, set_opcion_seleccionada),)
                
                return card
            finally:
                db.close()
        
        pag = html.div(
            {
                "style": {
                    "display": "flex",
                    "flex-direction": "column",
                    "justify-content": "center",
                    "align-items": "center",
                    "width": "100dvw",
                    "height": "100dvh"
                }
            },
            html.div(
                {
                    
                },
                html.i({"class_name": "material-icons", "style": {"font-size": "4rem"}}, "visibility")
            ),
            html.div(
                {
                    "class_name": "crud_container",
                    "style": {
                        "display": "flex",
                        "flex-direction": "row",
                        "gap": "1rem",
                        "background": COLORS["deep_gray"],
                        "padding": "1rem",
                        "width": "80dvw",
                        "height": "80dvh",
                        "borderRadius": "16px",
                        "boxShadow": "0 4px 30px rgba(0, 0, 0, 0.1)",
                        "backdropFilter": "blur(8px)",
                        "-webkit-backdrop-filter": "blur(8px)",
                        "border": "1px solid rgba(215, 215, 215, 0.3)",
                    }
                },
                html.div(
                    {
                        "class_name": "Cbuttons_container",
                        "style": {
                            "display": "flex",
                            "flex-direction": "column",
                            "justify-content": "flex-start",
                            "align-items": "center",
                            "gap": "2rem",
                            "width": "20%",
                            "background": hex_to_rgba(COLORS["dark_bg"], 0.8),
                            "borderRadius": "16px",
                            "boxShadow": "0 4px 30px rgba(0, 0, 0, 0.1)",
                            "backdropFilter": "blur(8px)",
                            "-webkit-backdrop-filter": "blur(8px)",
                            "border": "1px solid rgba(215, 215, 215, 0.3)",
                            "padding": "5px",
                        }
                    },
                    html.div(
                        {
                            "style": {
                                "width": "100%",
                                "max-width": "200px"
                            }
                        },
                        html.button(
                            {
                                "class_name": "create_button",
                                "on_click": lambda e: abrir_modal("Crear"),
                                "style": BUTTONS_STYLE
                            },
                            "+"
                        )
                    ),
                    html.div(
                        {
                            "class_name": "other_buttons",
                            "style": {
                                "display": "flex",
                                "flex-direction": "column",
                                "gap": "0.5rem",
                                "width": "100%",
                                "max-width": "200px"
                            }
                        },
                        html.button(
                            {
                                "on_click": lambda e: abrir_modal("Editar") if not opcion_seleccionada == None else cerrar_modal(),
                                "style": BUTTONS_STYLE
                            },
                            "Editar"
                        ),
                        html.button(
                            {
                                "on_click": lambda e: abrir_modal("Borrar") if not opcion_seleccionada == None else cerrar_modal(),
                                "style": BUTTONS_STYLE
                            },
                            "Borrar"
                        )
                    )
                ),
                html.div(
                    {
                        "class_name": "Ccards_container",
                        "style": {
                            "display": "flex",
                            "flex-direction": "column",
                            "width": "80%",
                            "overflow-y": "auto",
                            "background": hex_to_rgba(COLORS["dark_bg"], 0.8),
                            "borderRadius": "16px 5px 5px 16px",
                            "boxShadow": "0 4px 30px rgba(0, 0, 0, 0.1)",
                            "backdropFilter": "blur(8px)",
                            "-webkit-backdrop-filter": "blur(8px)",
                            "border": "1px solid rgba(215, 215, 215, 0.3)",
                            "padding": "5px",
                            "gap": "0.5rem"
                        }
                    },
                    proyectos()
                )
            ),
            modales(opcion_seleccionada, type_process, cerrar_modal, token) if activo_m else html.div()
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
        html.style(
            """
                .Ccards_container {
                    scrollbar-width: thin !important;
                    scrollbar-color: rgba(255, 255, 255, 0.2) transparent !important;
                }
                
                .Ccards_container::-webkit-scrollbar {
                    width: 6px !important; 
                }
                
                .Ccards_container::-webkit-scrollbar-track {
                    background: transparent !important; 
                    margin: 10px 0 !important; 
                }
                
                .Ccards_container::-webkit-scrollbar-thumb {
                    background-color: rgba(255, 255, 255, 0.2) !important; 
                    border-radius: 10px !important; 
                }
                
                .Ccards_container::-webkit-scrollbar-thumb:hover {
                    background-color: rgba(255, 255, 255, 0.4) !important; 
                }
                
                @media (max-width: 768px) {
                    .crud_container {
                        flex-direction: column !important;
                    }
                    .Ccards_container {
                        width: 100% !important;
                        height: 100% !important;
                    }
                    .Cbuttons_container {
                        width: 100% !important;
                        flex-direction: row !important;
                        justify-content: space-between !important;
                    }
                    .other_buttons {
                        flex-direction: row !important;
                    }
                    .titulo {
                        font-size: 0.8rem !important;
                    }
                }
            """
        ),
        login_pag() if not sesion else adminpanel_pag()
    )
    
    return pag

@component
def cards_elements(card_data, on_card_select):
    
    card = html.label(
        {
            "for": str(card_data.id),
            "style": {
                "display": "flex",
                "flex-direction": "row",
                "align-items": "center",
                "background": COLORS["degradado"],
                "borderRadius": "8px",
                "padding": "12px",
                "gap": "10px",
                "width": "100%"
            }
        },
        html.input(
            {
                "type": "radio",
                "id": str(card_data.id),
                "name": "grupo_opciones",
                "value": str(card_data.id),
                "on_change": lambda e: on_card_select(e["target"]["value"]),
                "style": {
                    "width": "17px",
                    "height": "17px",
                    "border-radius": "50%",
                }
            }
        ),
        html.div(
            {
                
                "style": {
                    "width": "100%"
                }
            },
            html.div(
                {
                    
                },
                html.p(
                    {
                        "class_name": "titulo",
                        "style": {
                            "display": "flex",
                            "flex-direction": "row",
                            "align-items": "center",
                            "gap": "10px",
                            "height": "100%",
                            "font-size": "1rem",
                        }
                    },
                    f"{card_data.titulo}",
                    html.i({"class_name": "material-icons", "style": {"font-size": "1rem"}}, "star")  if card_data.destacado else ""
                )
            )
        )
    )
    
    return card

@component
def modales(id, type_modal, on_close, token):
    db = SessionLocal()
    
    def modal_from():
        formulario, set_formulario = use_state({})
        mensaje_error, set_mensaje_error = use_state("")
        
        def datos_card():
            try:
                card = get_card(db, id)
                
                return card
            finally:
                db.close()

        def handle_change(campo):
            def update(e):
                valor = e["target"]["value"]
                
                if not campo == "":
                    set_formulario({**formulario, campo: valor})
                
            return update

        def handle_checkbox(e):
            set_formulario({**formulario, "destacado": e["target"]["checked"]})

        def enviar_datos(e):
            datos_finales = dict(formulario)
            
            if type_modal == "Crear" and "destacado" not in datos_finales:
                datos_finales["destacado"] = False
            
            if not token:
                set_mensaje_error("Error")
                return
            
            validacion = verificar_token(token)
            if not validacion["valido"]:
                set_mensaje_error(validacion["error"])
                return
            
            usuario = validacion["datos"]
            if usuario.get("usuario") != "admin":
                set_mensaje_error("No tienes permisos")
                return
            
            try:
                print("Diccionario listo para enviar:", datos_finales)
                if type_modal == "Crear":
                    try:
                        nuevo_proyecto = schemas.CardCreate(**datos_finales)
                        create_card(db, nuevo_proyecto)
                    finally:
                        db.close()
                elif type_modal == "Editar":
                    try:
                        proyecto_actualizado = schemas.CardUpdate(**datos_finales)
                        update_card(db, id, proyecto_actualizado)
                    finally:
                        db.close()
                on_close()
            except:
                set_mensaje_error("Error al crear el proyecto")

        campos_obligatorios = ["titulo", "descripcion_corta", "descripcion_larga", "url_imagen"]
        boton_desactivado = False
        if type_modal == "Crear":
            boton_desactivado = any(not formulario.get(campo, "").strip() for campo in campos_obligatorios)
        
        estilo_fondo = {
            "position": "fixed", "top": "0", "left": "0",
            "width": "100%", "height": "100dvh",
            "backgroundColor": "rgba(0, 0, 0, 0.5)",
            "display": "flex", "justifyContent": "center", "alignItems": "center"
        }
        
        estilo_caja = {
            "backgroundColor": COLORS["dark_bg"], "padding": "20px", "borderRadius": "8px",
            "display": "flex", "flexDirection": "column", "gap": "8px",
            "width": "400px", "boxShadow": "0 4px 8px rgba(0,0,0,0.2)"
        }
        
        estilo_input = {
            "width": "100%", "padding": "8px 11px", "background": "rgba(255, 255, 255, 0.05)", 
            "border": "1px solid rgba(255, 255, 255, 0.2)",
            "border-radius": "8px", "color": "#ffffff", "font-size": "0.7rem",
            "box-sizing": "border-box", "outline": "none"
        }

        moda = html.div(
            {
                "on_click": lambda event: on_close(),
                "style": estilo_fondo
            },
            html.div(
                {
                    "on_click": event(lambda e: None, stop_propagation=True),
                    "style": estilo_caja
                },
                html.h4(
                    {
                        "style": {
                            "margin": "0 0 10px 0",
                        }
                    }, 
                    f"{type_modal} Elemento"),
                
                html.label({"style": {"font-size": "0.7rem"}}, "Título:" if type_modal == "Editar" else "*Título:" ),
                html.input({"max_length": "55","type": "text", "value": datos_card().titulo if type_modal == "Editar" else "", "on_change": handle_change("titulo"), "style": estilo_input}),
                
                html.label({"style": {"font-size": "0.7rem"}}, "Enunciado:" if type_modal == "Editar" else "*Enunciado:"),
                html.input({"max_length": "75", "type": "text", "value": datos_card().descripcion_corta if type_modal == "Editar" else "", "on_change": handle_change("descripcion_corta"), "style": estilo_input}),
                
                html.label({"style": {"font-size": "0.7rem"}}, "Descripción:" if type_modal == "Editar" else "*Descripción:"),
                html.textarea({"value": datos_card().descripcion_larga if type_modal == "Editar" else "", "on_change": handle_change("descripcion_larga"), "rows": "4", "style": {
                        "width": "100%", "padding": "8px 11px", "background": "rgba(255, 255, 255, 0.05)",  
                        "border": "1px solid rgba(255, 255, 255, 0.2)", "border-radius": "8px", "color": "#ffffff", 
                        "font-size": "0.6rem", "box-sizing": "border-box", "outline": "none",
                        "min-height": "100px", "resize": "none", "font-family": "inherit", "margin": "0",
                    }}),
                
                html.label({"style": {"font-size": "0.7rem"}}, "URL Imagen:" if type_modal == "Editar" else "*URL Imagen:"),
                html.input({"type": "url", "value": datos_card().url_imagen if type_modal == "Editar" else "", "on_change": handle_change("url_imagen"), "style": estilo_input}),
                
                html.label(
                    {"style": {"font-size": "0.7rem", "display": "flex", "alignItems": "center", "justify-content": "flex-start", "gap": "5px", "marginTop": "5px"}},
                    html.input({
                        "type": "checkbox", 
                        "checked": formulario.get("destacado", datos_card().destacado if type_modal == "Editar" else False), 
                        "on_change": handle_checkbox
                    }),
                    "¿Destacado?"
                ),
                
                html.label({"style": {"font-size": "0.7rem", "marginTop": "5px"}}, "URL Descarga:"),
                html.input({"type": "url", "value": datos_card().url_descarga if type_modal == "Editar" else "", "on_change": handle_change("url_descarga"), "style": estilo_input}),
                
                html.label({"style": {"font-size": "0.7rem"}}, "URL Previa:"),
                html.input({"type": "url", "value": datos_card().url_previa if type_modal == "Editar" else "", "on_change": handle_change("url_previa"), "style": estilo_input}),
                
                html.button(
                    {
                        "on_click": enviar_datos,
                        "disabled": boton_desactivado,
                        "style": {
                            "marginTop": "15px", 
                            "padding": "10px", 
                            "backgroundColor": COLORS["primary"], 
                            "color": COLORS["dark_bg"], 
                            "border": "none", 
                            "borderRadius": "4px",
                            "cursor": "not-allowed" if boton_desactivado else "pointer",
                            "opacity": "0.5" if boton_desactivado else "1",
                            "pointerEvents": "none" if boton_desactivado else "auto"
                        }
                    },
                    f"{type_modal}" if mensaje_error == "" else f"{mensaje_error}"
                )
            )
        )
        
        return moda
    
    def modal_delete():
        mensaje_error, set_mensaje_error = use_state("")
        
        def eliminar_dato(event):
            if not token:
                set_mensaje_error("Error")
                return
        
            validacion = verificar_token(token)
            if not validacion["valido"]:
                set_mensaje_error(validacion["error"])
                return
        
            usuario = validacion["datos"]
            if usuario.get("usuario") != "admin":
                set_mensaje_error("No tienes permisos")
                return

            try:
                delete_card(db, id)
            except:
                set_mensaje_error("Error al eliminar")
            finally:
                db.close()
                on_close()
        
        moda = html.div(
            {
                "on_click": lambda event: on_close(),
                "style": {
                    "position": "fixed",
                    "top": "0",
                    "left": "0",
                    "width": "100vw",
                    "height": "100dvh",
                    "backgroundColor": "rgba(0, 0, 0, 0.7)",
                    "display": "flex",
                    "justifyContent": "center",
                    "alignItems": "center",
                    "zIndex": "9999"
                }
            },
            html.div(
                {
                    "on_click": event(lambda e: None, stop_propagation=True),
                    "style": {
                        "backgroundColor": COLORS["dark_bg"],
                        "padding": "50px 70px",
                        "borderRadius": "12px",
                        "display": "flex",
                        "flexDirection": "column",
                        "alignItems": "center",
                        "fontFamily": "sans-serif",
                        "boxShadow": "0 10px 15px rgba(0,0,0,0.3)"
                    }
                },
                html.h1(
                    {
                        "style": {
                            "color": "white",
                            "margin": "0 0 40px 0",
                            "fontSize": "3.5rem",
                            "fontWeight": "400"
                        }
                    },
                    "¿Seguro?"
                ),
                html.div(
                    {
                        "style": {
                            "display": "flex",
                            "gap": "15px",
                            "width": "100%",
                            "justifyContent": "center"
                        }
                    },
                    html.button(
                        {
                            "on_click": lambda event: eliminar_dato(event),
                            "style": {
                                "backgroundColor": "#c1121f", 
                                "color": "white",
                                "border": "none",
                                "padding": "15px 0",
                                "width": "140px",
                                "fontSize": "1.3rem",
                                "borderRadius": "6px",
                                "cursor": "pointer"
                            }
                        },
                        "si" if mensaje_error == "" else f"{mensaje_error}"
                    ),
                    html.button(
                        {
                            "on_click": lambda event: on_close(),
                            "style": {
                                "backgroundColor": "#2ecc71",
                                "color": "white",
                                "border": "none",
                                "padding": "15px 0",
                                "width": "140px",
                                "fontSize": "1.3rem",
                                "borderRadius": "6px",
                                "cursor": "pointer"
                            }
                        },
                        "no"
                    )
                )
            )
        )
        
        return moda
    
    modal = modal_delete() if type_modal == "Borrar" else modal_from()
    
    return modal
