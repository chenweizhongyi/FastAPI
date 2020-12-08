from sqlalchemy import Integer,String,Column

from project.dbbase import Base

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    username = Column(String,unique=True,index=True)
    hashpass = Column(String)
    email = Column(String,unique=True)


