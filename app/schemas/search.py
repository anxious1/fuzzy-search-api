from pydantic import BaseModel

class SearchItemOut(BaseModel):
    id: int
    content: str

    class Config:
        orm_mode = True
