from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud2, models2, schemas2
from .database2 import SessionLocal, engine

models2.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas2.User)
def create_user(user: schemas2.UserCreate, db: Session = Depends(get_db)):
    db_user = crud2.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud2.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas2.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud2.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas2.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud2.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas2.Item)
def create_item_for_user(
    user_id: int, item: schemas2.ItemCreate, db: Session = Depends(get_db)
):
    return crud2.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas2.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud2.get_items(db, skip=skip, limit=limit)
    return items

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,host = '127.0.0.1',port = 8000,log_level="info")