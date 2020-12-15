from sqlalchemy.orm import Session
from sqlalchemy import and_
from project import models, schemas,token_config
from datetime import timedelta
import jwt


def get_user(db : Session,username : str = None,hashpass:str =None):
    return db.query(models.Users).filter(
        and_(models.Users.hashpass == hashpass,models.Users.username == username)).first()


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