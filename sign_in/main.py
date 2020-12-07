from fastapi import FastAPI

from . import schemas

app = FastAPI()

@app.post('/login')
def login(user: schemas.Uesr):
    pass