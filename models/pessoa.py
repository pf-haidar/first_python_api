from pydantic import BaseModel


class Pessoa(BaseModel):
    nome: str