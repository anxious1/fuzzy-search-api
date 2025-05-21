# scripts/init_db.py

from app.db.session import engine, Base
from app.models.user import User
# если у вас есть другие модели, импортируйте их сюда:
# from app.models.corpus import Corpus

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ SQLite БД создана и таблицы инициализированы")

if __name__ == "__main__":
    init_db()
