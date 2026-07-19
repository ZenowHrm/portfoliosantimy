from sqlalchemy.orm import Session
from backend import schemas
import models
from fastapi import HTTPException

#-------- Lectura
def get_card(db: Session, card_id: int):
    return db.query(models.Card).filter(models.Card.id == card_id).first()

def get_destacadas(db: Session, limite: int = 5):
    return db.query(models.Card).filter(models.Card.destacado == True).limit(limite).all()

def get_recientes(db: Session, limite: int = 6):
    return db.query(models.Card).order_by(models.Card.fecha.desc()).limit(limite).all()

def get_cards(db: Session, skip: int = 0, limit: int = 12):
    return db.query(models.Card).order_by(models.Card.fecha.desc()).offset(skip).limit(limit).all()

#-------- Creacion
def create_card(db: Session, card: schemas.CardCreate):
    db_card = models.Card(
        titulo=card.titulo,
        descripcion_corta=card.descripcion_corta,
        descripcion_larga=card.descripcion_larga,
        url_imagen=card.url_imagen,
        destacado=card.destacado,
        url_descarga=card.url_descarga,
        url_previa=card.url_previa
    )
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card

#-------- Actualizar
def update_card(db: Session, card_id: int, card_update: schemas.CardUpdate):
    db_card = db.query(models.Card).filter(models.Card.id == card_id).first()
    if not db_card:
        return None
    update_data = card_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_card, key, value)
    db.commit()
    db.refresh(db_card)
    return db_card

#-------- Eliminar
def delete_card(db: Session, card_id: int):
    db_card = db.query(models.Card).filter(models.Card.id == card_id).first()
    if not db_card:
        return False
    db.delete(db_card)
    db.commit()
    return True