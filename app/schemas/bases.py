"""Schemas de repostas a consultas da API."""
from typing import List, Optional

from pydantic import BaseModel, Field, RootModel


class ItemLitros(BaseModel):
    """Modelo de item de litros."""

    CONTROL: Optional[str] = Field(examples=["VINHO DE MESA"])
    PRODUTO: Optional[str] = Field(examples=["TINTO"])
    ANO: Optional[str] = Field(examples=["1970"])
    L: Optional[float] = Field(examples=["1231456"])


class ItemKG(BaseModel):
    """Modelo de item de KG."""

    CONTROL: Optional[str] = Field(examples=["TINTAS"])
    CULTIVAR: Optional[str] = Field(examples=["TINTAS"])
    ANO: Optional[str] = Field(examples=["1970"])
    Kg: Optional[float] = Field(examples=["123456"])


class ItemValor(BaseModel):
    """Modelo de item de valor."""

    PAIS: Optional[str] = Field(examples=["Alemanha"])
    ANO: Optional[str] = Field(examples=["1970"])
    Kg: Optional[float] = Field(examples=["12345.0"])
    USD: Optional[float] = Field(examples=["1000.0"])


class Producao(RootModel[List[ItemLitros]]):
    """Modelo de resposta de produção."""

    pass


class Processamento(RootModel[List[ItemKG]]):
    """Modelo de resposta de processamento."""

    pass


class Comercializacao(RootModel[List[ItemLitros]]):
    """Modelo de resposta de comercialização."""

    pass


class Importacao(RootModel[List[ItemValor]]):
    """Modelo de resposta de importação."""

    pass


class Exportacao(RootModel[List[ItemValor]]):
    """Modelo de resposta de exportação."""

    pass
