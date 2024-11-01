import sqlalchemy
from sqlalchemy.orm import Session, sessionmaker
import logging

logger = logging.getLogger("main.app.utils.connection")

SQLALCHEMY_DATABASE_URL = 'sqlite:///storage/app/authentication.db'


Base = sqlalchemy.orm.declarative_base()


class DatabaseConnection:
    def __new__(self) -> Session:
        self._engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URL)
        Base.metadata.create_all(self._engine)
        logger.debug(
            f'DatabaseConnection - Sessão Iniciada {SQLALCHEMY_DATABASE_URL}')
        return sessionmaker(
            autocommit=False, autoflush=False, bind=self._engine)
