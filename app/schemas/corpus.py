from pydantic import BaseModel

class CorpusCreate(BaseModel):
    name: str
    content: str

class CorpusOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
