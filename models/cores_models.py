from core.configs import settings
from sqlalchemy import Column, Integer, String, Float, Boolean

class CoresModel(settings.DBBaseModel):
    __tablename__ = "cor"

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(256))
    hex: str = Column(String(7))
    red: int = Column(Integer())
    green: int = Column(Integer())
    blue: int = Column(Integer())
