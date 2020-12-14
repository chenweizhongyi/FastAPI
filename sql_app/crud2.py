from sqlalchemy.orm import Session

from . import models2, schemas2



def get_user(db: Session, user_id: int):
    return db.query(models2.User).filter(models2.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models2.User).filter(models2.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models2.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas2.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models2.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models2.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas2.ItemCreate, user_id: int):
    db_item = models2.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item