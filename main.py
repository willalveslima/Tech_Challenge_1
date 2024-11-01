"""Arquivo de inicialização da aplicação."""

import logging
import os

from logging.handlers import TimedRotatingFileHandler
from app.routers import consulta, authentication
from fastapi import FastAPI, Request


# Configurar o diretório de logs
LOG_DIRECTORY = "storage/logs"

if not os.path.exists(LOG_DIRECTORY):

    os.makedirs(LOG_DIRECTORY)


# Configurar o TimedRotatingFileHandler
log_file = os.path.join(LOG_DIRECTORY, "app.log")
handler = TimedRotatingFileHandler(
    log_file, when="midnight", interval=1, backupCount=2)
handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"))


# Configurar o logging
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[
        handler,
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('main.app')
http_logger = logging.getLogger("http.logger")


def create_app():
    """Cria a aplicação."""
    logger.info("Criando a aplicação...")
    app = FastAPI(
        title="Consulta Bases de Dados Embrapa",
        version="0.0.1",
    )

    app.include_router(authentication.router_user)
    app.include_router(consulta.consulta)

    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        """Logger de eventos http."""
        http_logger.info("Recebendo requisicao: %s %s",
                         request.method, request.url)
        response = await call_next(request)
        http_logger.info("Respondendo requisicao: %s", response.status_code)
        return response
    return app


logger.debug("Iniciando a aplicação...")


app = create_app()

logger.debug("Aplicação criada com sucesso!")
