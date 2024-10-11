from datetime import datetime

from http import HTTPStatus


from fastapi import Depends, HTTPException

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


from app.models import models

from app.utils.connection import DatabaseConnection

from app.utils.operations import SqlAlchemyRepository

from app.schemas.user import User, UserCreated, UserToken

from app.utils.authenticator import Authenticator


reuseable_oauth = OAuth2PasswordBearer(tokenUrl="v1/users/signin", scheme_name="JWT")



class AuthenticationService:

    def __init__(self):

        self._session = DatabaseConnection()

        self._repository = SqlAlchemyRepository(self._session)

        self._authenticator = Authenticator()


    async def signup(self, user: User) -> UserCreated:

        _user = self._repository.get_user_by_email(user.email)


        if _user:

            raise HTTPException(

                status_code=HTTPStatus.BAD_REQUEST.value,

                detail="User already registered",
            )


        user_created = self._repository.add(models.User(**user.dict()))

        return UserCreated(**user_created.__dict__)


    async def signin(self, user_login: OAuth2PasswordRequestForm) -> UserToken:

        user_from_db = self._repository.get_user_by_email(user_login.username)


        if not user_from_db:

            raise HTTPException(

                status_code=HTTPStatus.BAD_REQUEST.value, detail="User does not exist"
            )


        if not self._authenticator.verify_hashed_password(

            plain_password=user_login.password, hashed_password=user_from_db.password

        ):

            raise HTTPException(

                status_code=HTTPStatus.UNAUTHORIZED.value, detail="Invalid Credentials"
            )


        token_payload = self._authenticator.generate_jwt_token(user_from_db.email)


        return UserToken(access_token=token_payload["access_token"], user=user_from_db.email, exp=token_payload["exp"])


    async def get_token_header(self, token=Depends(reuseable_oauth)) -> UserCreated:

        token_payload = self._authenticator.decode_jwt_token(token)


        if datetime.fromtimestamp(token_payload["exp"]) < datetime.now():

            raise HTTPException(

                status_code=HTTPStatus.UNAUTHORIZED.value,

                detail="Token expired",
            )


        user = self._repository.get_user_by_email(token_payload["user"])


        if user is None:

            raise HTTPException(

                status_code=HTTPStatus.NOT_FOUND.value,

                detail="Could not find user",
            )


        return UserCreated(**user.__dict__)