"""Arquivo de inicialização da aplicação."""

import logging
import os
from logging.handlers import TimedRotatingFileHandler

import uvicorn

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
logger = logging.getLogger('main')


def main():
    """Executa a aplicação."""
    logger.info("Iniciando a aplicação...")
    uvicorn.run("app.app:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
