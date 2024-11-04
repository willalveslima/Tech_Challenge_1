"""Arquivo de inicialização da aplicação."""

import logging
import os
from logging.handlers import TimedRotatingFileHandler

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request

from app.routers import (authentication, comercializacao, exportacao,
                         importacao, processamento, producao)

# carregar variáveis de ambiente
load_dotenv()


ENABLE_LOG = eval(os.getenv("ENABLE_LOG"))

if ENABLE_LOG:
    # Configurar o diretório de logs
    LOG_DIRECTORY = os.getenv("LOG_DIRECTORY")

    if not os.path.exists(LOG_DIRECTORY):

        os.makedirs(LOG_DIRECTORY)

    # Configurar o TimedRotatingFileHandler
    log_file = os.path.join(LOG_DIRECTORY, "app.log")
    handler = TimedRotatingFileHandler(
        log_file, when="midnight", interval=1, backupCount=2)
    handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

    # Configurar o logging
    if eval(os.getenv("DEBUG")):
        level = logging.DEBUG
    else:
        level = logging.INFO
    logging.basicConfig(
        level=level,
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
        title="API - Tech Challenge 1 - FIAP",
        version="1.0.0",
        description=(
            "API para consulta Banco de dados de uva, vinho e derivados"
            "da Embrapa: <br>"
            '<a  href="http://vitibrasil.cnpuv.embrapa.br/index.php">'
            'http://vitibrasil.cnpuv.embrapa.br/index.php</a> .'
            "<br>Código fonte:"
            '<a  href="https://github.com/willalveslima/Tech_Challenge_1">'
            'https://github.com/willalveslima/Tech_Challenge_1</a>'
        ),

    )

    @app.get('/')
    def hello_world():
        return "Hello,World"
    app.include_router(authentication.router_user)
    app.include_router(producao.producao)
    app.include_router(processamento.processamento)
    app.include_router(comercializacao.comercializacao)
    app.include_router(importacao.importacao)
    app.include_router(exportacao.exportacao)

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

# uvicorn.run(app)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


