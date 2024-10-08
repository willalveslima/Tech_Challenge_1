"""Arquivo de inicialização da aplicação."""

import logging
import os
import uvicorn

# Configurar o diretório de logs
log_directory = "storage/logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configurar o logging
log_file = os.path.join(log_directory, "app.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

def main():
    """Executa a aplicação."""
    logging.info("Iniciando a aplicação...")
    uvicorn.run("app.app:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()