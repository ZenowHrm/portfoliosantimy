from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False, index=True)
    descripcion_corta = Column(String, nullable=False)
    descripcion_larga = Column(String, nullable=False)
    url_imagen = Column(String, nullable=False)
    destacado = Column(Boolean, default=False)
    fecha = Column(DateTime(timezone=True), server_default=func.now())
    url_descarga = Column(String, nullable=True)
    url_previa = Column(String, nullable=True)
