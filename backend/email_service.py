import smtplib
import os
import random
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def EnviarEmail(correo):
    load_dotenv() 

    remitente = os.getenv("USER")
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
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(remitente, os.getenv("PASS"))

        server.sendmail(remitente, destinatario, msg.as_string())
        server.quit()
        return True, str(code)
    except:
        return False, None
