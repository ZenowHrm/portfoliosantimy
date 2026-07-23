import hashlib
import hmac
import os
import datetime
import jwt
from dotenv import load_dotenv
from fastapi import Cookie, HTTPException

load_dotenv()

hash_guardado = str(os.getenv("HASH"))
SECRET_KEY = str(os.getenv("JWT_SECRET"))
ALGORITMO = "HS256"

def verificar_contrasena(contrasena_intento):
    intento_bytes = contrasena_intento.encode('utf-8')
    hash_intento = hashlib.sha256(intento_bytes).hexdigest()
    
    return hmac.compare_digest(hash_intento, hash_guardado)

def crear_token_acceso(datos: dict, minutos_validez: int = 60) -> str:
    payload = datos.copy()
    
    expiracion = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=minutos_validez)
    payload.update({"exp": expiracion})
    
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITMO)
    return token

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITMO])
        return {"valido": True, "datos": payload}
    except jwt.ExpiredSignatureError:
        return {"valido": False, "error": "El token ha expirado. Inicia sesión de nuevo."}
    except jwt.InvalidTokenError:
        return {"valido": False, "error": "Token inválido o alterado."}

def obtener_usuario(access_token: str = Cookie(None)):
    if not access_token:
        raise HTTPException(status_code=401, detail="No has iniciado sesion")
    
    validacion = verificar_token(access_token)
    if not validacion:
        HTTPException(status_code=401, detail=validacion["error"])
    
    return validacion["datos"]