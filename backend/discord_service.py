import os
import requests
from dotenv import load_dotenv

def EnviarDiscord(usuario, correo, mensaje):
    load_dotenv()
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    if not webhook_url:
        print("Error: No se encontró la URL del Webhook de Discord.")
        return False

    data = {
        # --- AQUÍ CONFIGURAS EL PERFIL DEL MENSAJE ---
        "username": "Portafolio | Notificaciones", # El nombre que aparecerá como remitente
        "avatar_url": "https://i.postimg.cc/9XvKhSNc/69-sin-titulo-20250129061922.png", # <-- URL pública de la foto de perfil
        
        "embeds": [
            {
                "title": "💡 ¡Nueva Idea / Consulta Recibida!",
                "color": 3447003, 
                "fields": [
                    {
                        "name": "👤 Usuario",
                        "value": usuario,
                        "inline": True
                    },
                    {
                        "name": "📧 Correo (Verificado)",
                        "value": correo,
                        "inline": True
                    },
                    {
                        "name": "📝 Mensaje",
                        "value": mensaje,
                        "inline": False
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            return True
        else:
            print(f"Error al enviar a Discord: {response.status_code}")
            return False
    except Exception as e:
        print(f"Excepción al conectar con Discord: {e}")
        return False