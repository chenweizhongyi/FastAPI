from sqlalchemy import Boolean,Integer,String,Column,ForeignKey

from .dbbase import Base

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    username = Column(String,unique=True,index=True)
    emali = Column(String,unique=True)
    hashpass = Column(String)
