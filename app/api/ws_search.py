from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.cruds.search import fuzzy_search

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.websocket("/ws/search")
async def websocket_search(websocket: WebSocket):
    await websocket.accept()
    db = SessionLocal()

    try:
        while True:
            data = await websocket.receive_text()
            results = fuzzy_search(db, query=data)
            response = [{"id": item.id, "content": item.content} for item in results]
            await websocket.send_json(response)
    except WebSocketDisconnect:
        await websocket.close()
    finally:
        db.close()
