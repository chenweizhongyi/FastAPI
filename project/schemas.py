from pydantic import BaseModel


class Uesr(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class Uesrcreat(Uesr):
    hashpass: str


class UesrBase(Uesr):
    id: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    sub: str