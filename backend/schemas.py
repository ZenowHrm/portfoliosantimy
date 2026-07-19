from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CardBase(BaseModel):
    titulo: str
    descripcion_corta: str
    descripcion_larga: str
    url_imagen: str
    destacado: bool = False
    url_descarga: Optional[str] = None
    url_previa: Optional[str] = None

class CardCreate(CardBase):
    pass

class CardUpdate(BaseModel):
    titulo: Optional[str] = None
    descripcion_corta: Optional[str] = None
    descripcion_larga: Optional[str] = None
    url_imagen: Optional[str] = None
    destacado: Optional[bool] = None
    url_descarga: Optional[str] = None
    url_previa: Optional[str] = None

class Card(CardBase):
    id: int
    fecha: datetime

    class Config:
        from_attributes = True