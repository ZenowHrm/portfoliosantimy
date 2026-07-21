import smtplib
import os
import random
import socket
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

old_getaddrinfo = socket.getaddrinfo
def new_getaddrinfo(*args, **kwargs):
    responses = old_getaddrinfo(*args, **kwargs)
    return [response for response in responses if response[0] == socket.AF_INET]
socket.getaddrinfo = new_getaddrinfo

def EnviarEmail(correo):
    load_dotenv() 

    remitente = os.getenv("EMAIL_USER")
    destinatario = correo
    asunto = "Codigo de verificacion"

    msg = MIMEMultipart()
    msg["Subject"] = asunto
    msg["From"] = remitente
    msg["To"] = destinatario
    
    code = random.randint(100000, 999999)

    try:
        with open("static/email.html", "r", encoding="UTF-8") as archivo:
            html = archivo.read()
        html = html.replace("negro", str(code))
    except FileNotFoundError:
        html = f"<h2>Tu código de verificación es: {code}</h2>"

    msg.attach(MIMEText(html, "html"))

    try:
        # 1. Usamos SMTP_SSL en el puerto 465 y le damos un límite de 10 segundos
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10)
        
        # 2. (IMPORTANTE) Eliminamos server.starttls() porque ya no es necesario
        
        server.login(remitente, os.getenv("PASS"))
        server.sendmail(remitente, destinatario, msg.as_string())
        server.quit()
        return True, str(code)
        
    except Exception as e:
        # 3. Imprimimos el error exacto para dejar de adivinar si vuelve a fallar
        print(f"Error crítico al enviar el correo: {e}")
        return False, None
