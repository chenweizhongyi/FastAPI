from sqlalchemy import create_engine

# 创建数据库引擎
SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL)