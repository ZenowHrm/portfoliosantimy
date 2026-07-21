import re
import asyncio
from reactpy import component, html, use_state
from theme import COLORS
from backend.email_service import EnviarEmail
from components.modal import EmailModal 
from backend.discord_service import EnviarDiscord

@component
def Ideas():
    user, set_user = use_state("")
    text, set_text = use_state("")
    email, set_email = use_state("")
    
    show_modal, set_show_modal = use_state(False)
    generated_code, set_generated_code = use_state("")
    modal_error, set_modal_error = use_state("")
    is_loading, set_is_loading = use_state(False)
    form_status, set_form_status = use_state({"type": "", "msg": ""}) 
    
    patron_correo = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    correo_valido = bool(re.match(patron_correo, email))
    is_disabled = not (user.strip() and text.strip() and correo_valido) or is_loading
    
    async def request_verification(event):
        if is_disabled:
            return
            
        set_is_loading(True)
        set_form_status({"type": "", "msg": ""})
        
        await asyncio.sleep(0.1)
        
        success, code = await asyncio.to_thread(EnviarEmail, email)
        
        set_is_loading(False)
        
        if success:
            set_generated_code(code)
            set_modal_error("")
            set_show_modal(True)
        else:
            set_form_status({"type": "error", "msg": "No se pudo enviar el código de verificación. Intenta nuevamente."})
            
    async def handle_verify(code_entered):
        if code_entered.strip() == generated_code:
            exito_discord = await asyncio.to_thread(EnviarDiscord, user, email, text)
            
            if exito_discord:
                set_show_modal(False)
                set_user("")
                set_text("")
                set_email("")
                set_generated_code("")
                set_form_status({"type": "success", "msg": "¡Mensaje enviado exitosamente!"})
            else:
                set_show_modal(False)
                set_form_status({"type": "error", "msg": "Verificación exitosa, pero hubo un error al guardar tu mensaje. Intenta luego."})
                
        else:
            set_modal_error("El código es incorrecto. Por favor, verifica tu correo.")
    def handle_close_modal():
        set_show_modal(False)
        set_modal_error("")
    
    ideas = html.div(
        {
            "style": { "position": "relative" }
        },
        html.style(
            """
                @media (max-width: 657px) {
                    .texto { font-size: 0.8rem !important; } 
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
            html.h3({"style": {"text-align": "center"}}, "Do you have any ideas or projects in mind?"),
            html.p(
                {"style": {"text-align": "center", "font-size": "0.8rem", "padding": "10px 0 0 0"}},
                "Si tienes alguna idea que quieras compartir, escríbela aquí. También puedes usar este espacio para contactarme si te interesa que colaboremos y desarrollemos algún proyecto juntos."
            ),
            html.div(
                {"style": {"display": "flex", "flex-direction": "column", "padding": "20px", "width": "100%", "box-sizing": "border-box"}},
                
                # --- INPUT USUARIO ---
                html.p({}, "Usuario"),
                html.input({
                    "max_length": "20",
                    "type": "text", "placeholder": "Nombre de Usuario", "value": "",  
                    "on_change": lambda e: set_user(e["target"]["value"]),
                    "style": {
                        "width": "100%", "padding": "12px 15px", "background": "rgba(255, 255, 255, 0.05)",  
                        "border": "1px solid rgba(255, 255, 255, 0.2)", "border-radius": "8px", "color": "#ffffff", 
                        "font-size": "0.8rem", "box-sizing": "border-box", "outline": "none"
                    }
                }),
                
                # --- INPUT IDEA ---
                html.p({"style": {"margin": "10px 0 0 0"}}, "Idea / Consulta"),
                html.textarea({
                    "max_length": "1000",
                    "placeholder": "Escribe aquí", "value": "",  
                    "on_change": lambda e: set_text(e["target"]["value"]), 
                    "style": {
                        "width": "100%", "padding": "12px 15px", "background": "rgba(255, 255, 255, 0.05)",  
                        "border": "1px solid rgba(255, 255, 255, 0.2)", "border-radius": "8px", "color": "#ffffff", 
                        "font-size": "0.8rem", "box-sizing": "border-box", "outline": "none",
                        "min-height": "150px", "resize": "none", "font-family": "inherit", "margin": "0 0 10px 0",
                    }
                }),
                
                # --- AVISO Y INPUT CORREO ---
                html.div(
                    {
                        "style": {
                            "box-sizing": "border-box", "background": COLORS.get("medium_gray", "#333"),
                            "padding": "1rem", "border-radius": "20px", "width": "100%",
                            "box-shadow": "0px 10px 30px rgba(0,0,0,0.5)", "margin": "auto", 
                        }
                    },
                    html.p({"class-name": "texto", "style": {"margin": "0"}}, "Por motivos de seguridad, ingresa tu correo electrónico para una verificación")
                ),
                html.p({"style": {"margin": "10px 0 0 0"}}, "Correo"),
                html.input({
                    "type": "email", "placeholder": "example@gmail.com", "value": "",
                    "on_change": lambda e: set_email(e["target"]["value"]),
                    "style": {
                        "width": "100%", "padding": "12px 15px", "background": "rgba(255, 255, 255, 0.05)", 
                        "border": "1px solid rgba(255, 255, 255, 0.2)" if (correo_valido or email == "") else "1px solid #ff4444",
                        "border-radius": "8px", "color": "#ffffff", "font-size": "0.8rem",
                        "box-sizing": "border-box", "outline": "none"
                    }
                })
            ),
            
            # --- MENSAJE DE ESTADO (Errores o Éxitos) ---
            html.p(
                {
                    "style": {
                        "color": "#4CAF50" if form_status["type"] == "success" else "#ff4444",
                        "font-size": "0.7rem",
                        "margin-bottom": "10px",
                        "text-align": "center",
                        "min-height": "20px"
                    }
                },
                form_status["msg"] if form_status["msg"] else ""
            ),
            
            # --- BOTÓN DE ENVIAR ---
            html.button(
                {
                    "on_click": request_verification,
                    "disabled": is_disabled,  
                    "style": {
                        "display": "flex", "font-size": "1rem", "flex-direction": "row", 
                        "justify-content": "center", "align-items": "center",
                        "background": COLORS["dark_bg"], "width": "250px",
                        "border": "1px solid rgba(255, 255, 255, 0.08)", "border-radius": "4px",
                        "padding": "10px",
                        "opacity": "0.5" if is_disabled else "1",  
                        "cursor": "not-allowed" if is_disabled else "pointer", 
                    }
                },
                "Procesando..." if is_loading else "Send"
            )
        )
    )
    
    # Retornamos el contenedor con el formulario y, si el estado lo dicta, montamos el modal
    return html.div(
        ideas,
        EmailModal(
            on_close=handle_close_modal, 
            on_verify=handle_verify, 
            error_msg=modal_error
        ) if show_modal else ""
    )