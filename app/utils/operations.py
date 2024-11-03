"""This module contains the repository classes for the application."""
import abc

from sqlalchemy.orm import Session

from app.models import models


class AbstractRepository(abc.ABC):
    """Interface for the repository classes."""

    @abc.abstractmethod
    def add(self, model):
        """Add a model to the session."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_user_by_email(self, email: str):
        """Return a user by email."""
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    """Class that implements the repository interface using SQLAlchemy."""

    def __init__(self, session: Session):
        """Initialize the repository with a SQLAlchemy."""
        self._session = session()

    def add(self, model):
        """Add a model to the session."""
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)

        return model

    def get_user_by_email(self, email: str):
        """Return a user by email."""
        return (
            self._session.query(models.User)
            .filter_by(email=email)
            .one_or_none()
        )
