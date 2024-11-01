from http import HTTPStatus
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import User, UserCreated, UserToken
from app.services.authentication import AuthenticationService
import logging

router_user = APIRouter(prefix="/users", tags=["Users"])

logger = logging.getLogger("main.app.router.authentication")


@router_user.post(
    "/signup", status_code=HTTPStatus.CREATED.value, response_model=UserCreated
)
async def signup_user(user: User) -> JSONResponse:
    logger.debug("Chamada /signup - funcao signup_user")
    user_created = await AuthenticationService().signup(user)
    return JSONResponse(
        user_created.dict(), status_code=HTTPStatus.CREATED.value)


@router_user.post(
    "/signin", status_code=HTTPStatus.OK.value, response_model=UserToken
)
async def signin_user(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
) -> JSONResponse:
    logger.debug("Chamada /signin - funcao signin_user")
    token_jwt = await AuthenticationService().signin(user_credentials)
    return JSONResponse(token_jwt.dict(), status_code=HTTPStatus.OK.value)


@router_user.get(
    "/me", status_code=HTTPStatus.OK.value, response_model=UserCreated)
async def me(
    user: UserCreated = Depends(AuthenticationService().get_token_header),
) -> JSONResponse:
    logger.debug("Chamada /me - funcao me")
    return JSONResponse(user.dict(), status_code=HTTPStatus.OK.value)
