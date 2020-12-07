from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建数据库引擎
SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})

# 创建数据库回话
Session = sessionmaker(autocommit=True,autoflush=True,bind=engine)

# 声明一个Base类，用于定义映射类
Base = declarative_base()