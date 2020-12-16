from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')

# token配置
SECRET_KEY = "629fbf5adaeaa5773259e49d0d5fd8fbb764ac67187184b6460409c5a6ddad78"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1