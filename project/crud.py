from sqlalchemy.orm import Session
from sqlalchemy import and_
from project import models, schemas,token_config,dbbase
from datetime import timedelta
from fastapi import Depends

import jwt

models.Base.metadata.create_all(bind=dbbase.engine)

def create_session():
    db = dbbase.Sessionloc()
    try:
        yield db
    finally:
        db.close()

def cheok_user(db : Session,username : str = None,hashpass:str =None):
    return db.query(models.Users).filter(
        and_(models.Users.hashpass == hashpass,models.Users.username == username)).first()

def get_users(db : Session):
    return (db.query(models.Users.username,models.Users.email).all())

def get_user(db : Session,username : str = None):
    return db.query(models.Users).filter(
        (models.Users.username == username)).first()

def creat_user(db : Session, user: schemas.Uesrcreat):
    # hash_pass = user.hashpass + 'rrr'
    session_data = models.Users(username=user.username, hashpass=user.hashpass,email=user.email)
    db.add(session_data)
    db.commit()
    db.refresh(session_data)
    return session_data

def creat_user_token(user_data: dict,expires_delta: timedelta = None):
    if expires_delta:
        pass
    jwt_token = jwt.encode(user_data,token_config.SECRET_KEY,algorithm=token_config.ALGORITHM)
    return jwt_token

# 获取当前用户信息
def get_current_active_user(token: str = Depends(token_config.oauth2_scheme)):
    user_dict = jwt.decode(token,token_config.SECRET_KEY,algorithms=[token_config.ALGORITHM])
    from_suser = user_dict.get('sub')
    return from_suser