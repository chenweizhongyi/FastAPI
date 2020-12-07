from sqlalchemy.orm import Session
from . import models,schemas

def get_user(db : Session,username : str):
    return db.query(models.Users).filter(models.Users.username == username).first()

def creat_user(db : Session,user: schemas.Uesrcreat):
    hash_pass = user.hashpass + ''
    session_data = models.Users(username=user.username,emali=user.email,hashpass=hash_pass)
    db.add(session_data)
    db.commit()
    db.refresh(session_data)
    return session_data