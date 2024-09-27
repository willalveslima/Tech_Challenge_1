"""API com autenticação em fastapi."""
from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel

from app.constants import URL_BASE_PRODUCAO
from app.utils import convertar_para_json, ler_base_dados_csv

# Configurações
SECRET_KEY = "B1gS3cr3tK3y"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Modelos
class Token(BaseModel):
    """
    Token _summary_.

    Args:
        BaseModel (_type_): _description_
    """
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """.TokenData _summary_"""
    username: Optional[str] = None

class User(BaseModel):
    """
    User _summary_

    Args:
        BaseModel (_type_): _description_
    """
    username: str

class UserInDB(User):
    """
    UserInDB _summary_

    Args:
        User (_type_): _description_
    """
    hashed_password: str

# Usuários fictícios
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "hashed_password": "fakehashedpassword",
    }
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

def verify_password(plain_password, hashed_password):
    """
    verify_password _summary_

    Args:
        plain_password (_type_): _description_
        hashed_password (bool): _description_

    Returns:
        _type_: _description_
    """
    return plain_password == hashed_password

def get_user(db, username: str):
    """
    get_user _summary_

    Args:
        db (_type_): _description_
        username (str): _description_

    Returns:
        _type_: _description_
    """
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    """
    authenticate_user _summary_

    Args:
        fake_db (_type_): _description_
        username (str): _description_
        password (str): _description_

    Returns:
        _type_: _description_
    """
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/producao")
async def get_producao(current_user: User = Depends(get_current_user)) -> str:
    """
    get_producao executa a leitura da base de produção e retorna os dados em formato JSON.

    Returns:
        JSON: retorna os dados da base de produção em formato JSON.
    """
    df_producao = ler_base_dados_csv(URL_BASE_PRODUCAO)
    return convertar_para_json(df_producao)
