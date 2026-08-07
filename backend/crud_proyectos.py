import os
from types import SimpleNamespace
from backend import schemas
from fastapi import HTTPException
from backend.supabase_client import supabase

# Helper to convert row dicts into objects with attribute access
def _row_to_obj(row: dict):
    if row is None:
        return None
    return SimpleNamespace(**row)

#-------- Lectura
def get_card(card_id: int = None):
    """Obtener una tarjeta por id. db param kept for compatibility but ignored."""
    try:
        if card_id is None:
            return None
        res = supabase.table('portafolio').select('*').eq('id', card_id).execute()
        data = getattr(res, 'data', None) or (res.get('data') if isinstance(res, dict) else None)
        error = getattr(res, 'error', None) or (res.get('error') if isinstance(res, dict) else None)
        if error:
            raise Exception(error)
        if not data:
            return None
        # data can be a list or a single dict
        row = data[0] if isinstance(data, list) else data
        return _row_to_obj(row)
    except Exception as e:
        # Log or re-raise as HTTPException to be consistent with FastAPI usage
        raise HTTPException(status_code=500, detail=f"Error fetching card: {str(e)}")

def get_destacadas(limite: int = 5):
    try:
        res = supabase.table('portafolio').select('*').eq('destacado', True).order('fecha', desc=True).range(0, max(0, limite-1)).execute()
        data = getattr(res, 'data', None) or (res.get('data') if isinstance(res, dict) else None)
        error = getattr(res, 'error', None) or (res.get('error') if isinstance(res, dict) else None)
        if error:
            raise Exception(error)
        if not data:
            return []
        return [_row_to_obj(r) for r in data]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching destacadas: {str(e)}")

def get_recientes(limite: int = 6):
    try:
        res = supabase.table('portafolio').select('*').order('fecha', desc=True).range(0, max(0, limite-1)).execute()
        data = getattr(res, 'data', None) or (res.get('data') if isinstance(res, dict) else None)
        error = getattr(res, 'error', None) or (res.get('error') if isinstance(res, dict) else None)
        if error:
            raise Exception(error)
        if not data:
            return []
        return [_row_to_obj(r) for r in data]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching recientes: {str(e)}")

def get_cards(skip: int = 0, limit: int = 12):
    try:
        # Supabase uses range(offset, offset+limit-1)
        start = max(0, skip)
        end = max(0, skip + limit - 1)
        res = supabase.table('portafolio').select('*').order('fecha', desc=True).range(start, end).execute()
        data = getattr(res, 'data', None) or (res.get('data') if isinstance(res, dict) else None)
        error = getattr(res, 'error', None) or (res.get('error') if isinstance(res, dict) else None)
        if error:
            raise Exception(error)
        if not data:
            return []
        return [_row_to_obj(r) for r in data]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching cards: {str(e)}")

#-------- Creacion
def create_card(card: schemas.CardCreate = None):
    try:
        payload = card.dict() if hasattr(card, 'dict') else dict(card)
        # Remove id if present
        payload.pop('id', None)
        res = supabase.table('portafolio').insert(payload).select('*').execute()
        data = getattr(res, 'data', None) or (res.get('data') if isinstance(res, dict) else None)
        error = getattr(res, 'error', None) or (res.get('error') if isinstance(res, dict) else None)
        if error:
            raise Exception(error)
        if not data:
            raise Exception('No data returned after insert')
        return _row_to_obj(data[0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating card: {str(e)}")

#-------- Actualizar
def update_card(card_id: int = None, card_update: schemas.CardUpdate = None):
    try:
        if card_id is None:
            return None
        update_data = card_update.dict(exclude_unset=True) if hasattr(card_update, 'dict') else dict(card_update)
        if not update_data:
            return None
        res = supabase.table('portafolio').update(update_data).eq('id', card_id).select('*').execute()
        data = getattr(res, 'data', None) or (res.get('data') if isinstance(res, dict) else None)
        error = getattr(res, 'error', None) or (res.get('error') if isinstance(res, dict) else None)
        if error:
            raise Exception(error)
        if not data:
            return None
        return _row_to_obj(data[0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating card: {str(e)}")

#-------- Eliminar
def delete_card(card_id: int = None):
    try:
        if card_id is None:
            return False
        res = supabase.table('portafolio').delete().eq('id', card_id).execute()
        error = getattr(res, 'error', None) or (res.get('error') if isinstance(res, dict) else None)
        if error:
            raise Exception(error)
        return True
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting card: {str(e)}")