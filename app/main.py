from fastapi import FastAPI, Query
from sqlalchemy.orm import joinedload
from app.database import SessionLocal, init_db
from app.models import Quote, Tag

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

@app.get("/quotes")
def get_quotes(author: str = None, tag: str = None, search: str = None):
    db = SessionLocal()
    query = db.query(Quote).options(joinedload(Quote.tags))

    if author:
        query = query.filter(Quote.author.ilike(f"%{author}%"))

    if search:
        query = query.filter(Quote.text.ilike(f"%{search}%"))

    if tag:
        query = query.join(Quote.tags).filter(Tag.name.ilike(f"%{tag}%"))

    results = []
    for quote in query.all():
        results.append({
            "id": quote.id,
            "text": quote.text,
            "author": quote.author,
            "tags": [t.name for t in quote.tags]
        })

    db.close()
    return results
