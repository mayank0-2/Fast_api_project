from sqlalchemy.orm import session
from models import Inventory
from schemas import InventoryCreate, InventoryUpdate, InventoryBase


def get_inventory(db: session, skip: int = 0, limit: int = 100):
    return db.query(Inventory).offset(skip).limit(limit).all()


def get_inventory(db: session, user_id : int) :
    return db.query(Inventory).filter(models.Inventory.id == user_id).first()


def create_item(db: Session, user: schemas.InventoryCreate):
    db_user = models.Inventory(name = user.name, quantity = user.quantity)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_item(db: Session, user_id : int) :
    db_del = models.Inventory().filter(models.Inventory.id == user_id)
    db.delete(db_del)
    db.commit()
    db.refresh(db_del)
    return db_del