import os
from dotenv import load_dotenv
from supabase import create_client

# Carga variables .env (si no están en el entorno ya)
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError("SUPABASE_URL and SUPABASE_KEY must be set in the environment")

# Cliente Supabase global (reutilizable)
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Exportar supabase como cliente compartido desde este módulo
__all__ = ["supabase"]
