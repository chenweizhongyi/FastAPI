print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

from fastapi import FastAPI,Depends,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from project import models,crud,schemas
from project.dbbase import engine,Sessionloc

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def create_session():
    db = Sessionloc()
    try:
        yield db
    finally:
        db.close()


# 注册
@app.post('/logon',response_model=schemas.UesrBase)
def create_user(user_data:schemas.Uesrcreat,db:Session = Depends(create_session)):
    is_username = crud.get_user(db,username=user_data.username)
    if is_username:
        raise HTTPException(status_code=400, detail="用户名已经存在")
    return crud.creat_user(db,user=user_data)

# 登录
@app.post('/login',response_model=schemas.UesrBase)
def login(from_data:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(create_session)):
    get_username = crud.get_user(db,username=from_data.username,hashpass=from_data.password)
    if get_username is None:
        raise HTTPException(status_code=404,detail='账号不存在')
    return get_username

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,host = '127.0.0.1',port = 8000,log_level="info")