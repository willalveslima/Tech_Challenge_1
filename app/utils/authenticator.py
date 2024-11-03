"""Classe responsável por gerar e validar tokens JWT."""
import datetime
import logging
import os
from http import HTTPStatus

from fastapi.exceptions import HTTPException
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET = os.getenv("SECRET")
logger = logging.getLogger("main.app.utils.authenticator")


class Authenticator:
    """Classe responsável por gerar e validar tokens JWT."""

    def __init__(self):
        """Inicializa o objeto."""
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_hashed_password(
            self, plain_password: str, hashed_password: str):
        """Verifica se a senha informada é a mesma que a senha armazenada."""
        logger.debug("verify_hashed_password")
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_hashed_password(self, password: str):
        """Retorna a senha criptografada."""
        logger.debug("get_hashed_password")
        return self.pwd_context.hash(password)

    def generate_jwt_token(self, email):
        """Gera um token JWT."""
        jwt_payload = {
            "user": email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        }
        jwt_token = jwt.encode(jwt_payload, SECRET, algorithm="HS256")
        logger.debug(f'generate_jwt_token user {jwt_payload["user"]}')
        return {
            "access_token":  jwt_token,
            "user": jwt_payload["user"],
            "exp": str(jwt_payload["exp"])
        }

    def decode_jwt_token(self, token):
        """Decodifica um token JWT."""
        try:
            jwt_payload = jwt.decode(token, SECRET, algorithms=["HS256"])
            logger.debug("decode_jwt_token : token decoded.")
            return jwt_payload
        except JWTError:
            erro = "Could not validate credentials"
            logger.error(f'decode_jwt_token : {erro}')
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN.value,
                detail=erro,
                headers={"WWW-Authenticate": "Bearer"},
            )
