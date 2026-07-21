import os
import random
import resend
from dotenv import load_dotenv

def EnviarEmail(correo):
    # Cargar las variables de entorno
    load_dotenv() 

    # Asignar la API Key a Resend usando la variable solicitada
    resend.api_key = os.getenv("API_KEY_RESEND")
    
    # Importante: En Resend, el remitente ("From") debe ser de un dominio que hayas verificado.
    # Si estás haciendo pruebas y no tienes dominio, usa "onboarding@resend.dev".
    remitente = os.getenv("EMAIL_USER", "onboarding@resend.dev")
    destinatario = correo
    asunto = "Codigo de verificacion"
    
    # Generar código de 6 dígitos
    code = random.randint(100000, 999999)

    # Preparar el contenido HTML
    try:
        with open("static/email.html", "r", encoding="UTF-8") as archivo:
            html = archivo.read()
        html = html.replace("negro", str(code))
    except FileNotFoundError:
        html = f"<h2>Tu código de verificación es: {code}</h2>"

    # Construir el diccionario de parámetros para Resend
    params = {
        "from": remitente,
        "to": [destinatario],
        "subject": asunto,
        "html": html
    }

    # Enviar el correo
    try:
        resend.Emails.send(params)
        return True, str(code)
        
    except Exception as e:
        print(f"Error crítico al enviar el correo con Resend: {e}")
        return False, None