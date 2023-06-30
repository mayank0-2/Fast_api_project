from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import session
from . import crud, models, schemas
from .db import sessionlocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = sessionlocal()
    try :
        yield db
    finally:    
        db.close()
        
        


@app.get("/users/{user_id}", response_model=schemas.UsInventoryBase)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_inventory(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.InventoryCreate)
def create_item_for_user(
    item: schemas.InventoryCreate, db: Session = Depends(get_db)
):
    return create_item(db=db, item=item, user_id=user_id)


@app.delete("/users/{user_id}/items/", response_model=schemas.InventoryBase)
def delete_item_for_user(item: schemas.InventoryBase, db: Session = Depends(get_db)):
    
    return crud.delete_item(db=db, user_id=user_id)