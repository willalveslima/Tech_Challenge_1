from datetime import datetime
from http import HTTPStatus
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.models import models
from app.utils.connection import DatabaseConnection
from app.utils.operations import SqlAlchemyRepository
from app.schemas.user import User, UserCreated, UserToken
from app.utils.authenticator import Authenticator
import logging

logger = logging.getLogger("main.app.services.authentication")

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/users/signin", scheme_name="JWT")


class AuthenticationService:

    def __init__(self):
        self._session = DatabaseConnection()
        self._repository = SqlAlchemyRepository(self._session)
        self._authenticator = Authenticator()

    async def signup(self, user: User) -> UserCreated:

        _user = self._repository.get_user_by_email(user.email)
        if _user:
            erro = "User already registered"
            logger.error(f'signup user {user.email}: {erro}')
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST.value,
                detail=erro,
            )

        user_created = self._repository.add(models.User(**user.dict()))
        logger.debug(f'signup user {user.email}: User created')
        return UserCreated(**user_created.__dict__)

    async def signin(self, user_login: OAuth2PasswordRequestForm) -> UserToken:
        user_from_db = self._repository.get_user_by_email(user_login.username)
        if not user_from_db:
            erro = "User does not exist"
            logger.error(f'signin user {user_login.username}: {erro}')
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST.value,
                detail=erro
            )

        if not self._authenticator.verify_hashed_password(
            plain_password=user_login.password,
            hashed_password=user_from_db.password
        ):
            erro = "Invalid Credentials"
            logger.error(f'signin user {user_login.username}: {erro}')
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED.value,
                detail=erro
            )

        token_payload = self._authenticator.generate_jwt_token(
            user_from_db.email)
        logger.debug(f'signin user {user_login.username}: Token generated')
        return UserToken(access_token=token_payload["access_token"],
                         user=user_from_db.email, exp=token_payload["exp"])

    async def get_token_header(
            self, token=Depends(reuseable_oauth)) -> UserCreated:
        token_payload = self._authenticator.decode_jwt_token(token)
        if datetime.fromtimestamp(token_payload["exp"]) < datetime.now():
            erro = "Token expired"
            logger.error(f'get_token_header: {erro}')
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED.value,
                detail=erro,
            )

        user = self._repository.get_user_by_email(token_payload["user"])

        if user is None:
            erro = "User not found"
            logger.error(
                f'get_token_header user {token_payload["user"]}: {erro}')
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND.value,
                detail="Could not find user",
            )
        logger.debug(f'get_token_header user {
                     token_payload["user"]}: Token verified')
        return UserCreated(**user.__dict__)
