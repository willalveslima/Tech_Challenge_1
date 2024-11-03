"""Módulo de conexão com o banco de dados."""
import logging
import os

import sqlalchemy
from sqlalchemy.orm import Session, sessionmaker

logger = logging.getLogger("main.app.utils.connection")

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")


Base = sqlalchemy.orm.declarative_base()


class DatabaseConnection:
    """Classe de conexão com o banco de dados."""

    def __new__(self) -> Session:
        """Cria uma sessão com o banco de dados."""
        self._engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URL)
        Base.metadata.create_all(self._engine)
        logger.debug(
            f'DatabaseConnection - Sessão Iniciada {SQLALCHEMY_DATABASE_URL}')
        return sessionmaker(
            autocommit=False, autoflush=False, bind=self._engine)
