from sqlalchemy import Column, Integer, String
from app.db.session import Base

class SearchItem(Base):
    __tablename__ = "search_items"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)