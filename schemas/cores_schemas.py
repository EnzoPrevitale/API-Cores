from typing import Optional
from pydantic import BaseModel as SCBaseModel

class CorSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    hex: str
    red: int
    green: int
    blue: int

    class Config:
        orm_mode = True
        