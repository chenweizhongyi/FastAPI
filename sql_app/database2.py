from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建sql链接
SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# 创建sqlalchemy“引擎”
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False}
)

# 创建sqlalchemyLocal会话
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# 创建BASE类
Base = declarative_base()