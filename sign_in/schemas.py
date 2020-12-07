from pydantic import BaseModel

class Uesr(BaseModel):
    username : str
    email : str

class Uesrcreat(Uesr):
    hashpass :str