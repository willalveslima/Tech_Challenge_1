import datetime
from http import HTTPStatus
import logging
from jose import JWTError, jwt 
from fastapi.exceptions import HTTPException
from passlib.context import CryptContext


SECRET = "B4FvQWnTp718vr6AHyvdGlrHBGNcvuM4y3jUeRCgXxIwBZIbt"
logger = logging.getLogger("main.app.utils.authenticator")

class Authenticator:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_hashed_password(self, plain_password: str, hashed_password: str):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_hashed_password(self, password: str):
        return self.pwd_context.hash(password)

    def generate_jwt_token(self, email):
        jwt_payload = {
            "user": email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        }
        jwt_token = jwt.encode(jwt_payload, SECRET, algorithm="HS256")
        
        return  {
            "access_token" :  jwt_token,
            "user" : jwt_payload["user"],
            "exp" : str(jwt_payload["exp"])
        }

    def decode_jwt_token(self, token):
        try:
            jwt_payload = jwt.decode(token, SECRET, algorithms=["HS256"])
            return jwt_payload
        except JWTError:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN.value,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
