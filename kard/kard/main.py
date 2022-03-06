from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlmodel import Session, select
from typing import Optional, List

from kard.utils import setup_database
from kard.models import (
    DeckRead,
    DeckReadDetailed,
    DeckBase,
    CardRead,
    CardBase,
    CardReadDetailed,
    ReviewSessionBase,
    ReviewSessionReadDetailed,
    ReviewedCardBase,
    ReviewedCardRead,
    ReviewedCardReadDetailed,
)
from kard import crud


app = FastAPI()

SessionLocal = setup_database()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def hello_world():
    return {"Hello": "World"}


@app.get("/decks/", response_model=List[DeckRead], tags=["Decks"])
def read_decks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    decks = crud.get_decks(db, skip=skip, limit=limit)
    return decks


@app.post("/decks/", response_model=DeckReadDetailed, tags=["Decks"])
def create_deck(deck: DeckBase, db: Session = Depends(get_db)):
    s_deck = crud.get_deck_by_name(db, deck.name)
    if s_deck:
        raise HTTPException(
            status_code=400, detail="Deck with this name already exists"
        )
    return crud.create_deck(db, deck)


@app.get("/decks/{deck_id}/", response_model=DeckReadDetailed, tags=["Decks"])
def read_deck(deck_id: int, db: Session = Depends(get_db)):
    s_deck = crud.get_deck_by_id(db, deck_id)
    if not s_deck:
        raise HTTPException(status_code=404, detail="Deck not found")
    return s_deck


@app.get("/cards/", response_model=List[CardRead], tags=["Cards"])
def read_cards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cards = crud.get_cards(db, skip=skip, limit=limit)
    return cards


@app.post("/cards/", response_model=CardReadDetailed, tags=["Cards"])
def create_card(card: CardBase, db: Session = Depends(get_db)):
    return crud.create_card(db, card)


@app.get("/cards/{card_id}/", response_model=CardReadDetailed, tags=["Cards"])
def read_card(card_id: int, db: Session = Depends(get_db)):
    s_card = crud.get_card_by_id(db, card_id)
    if not s_card:
        raise HTTPException(status_code=404, detail="Card not found")
    return s_card


# @app.put("/cards/{card_id}/", response_model=CardReadDetailed, tags=["Cards"])
# def update_card(card_id: int, card: CardBase, db: Session = Depends(get_db)):
#     s_card = crud.get_card_by_id(db, card_id)
#     if not s_card:
#         raise HTTPException(status_code=404, detail="Card not found")
#     return crud.update_card(db, card)


@app.get(
    "/reviewed_cards/", response_model=List[ReviewedCardRead], tags=["Reviewed Cards"]
)
def read_reviewed_cards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cards = crud.get_reviewed_cards(db, skip=skip, limit=limit)
    return cards


@app.get(
    "/reviewed_cards/{reviewed_card_id}/",
    response_model=ReviewedCardReadDetailed,
    tags=["Reviewed Cards"],
)
def read_reviewed_card(reviewed_card_id: int, db: Session = Depends(get_db)):
    s_card = crud.get_reviewed_card_by_id(db, reviewed_card_id)
    if not s_card:
        raise HTTPException(status_code=404, detail="Reviewed Card not found")
    return s_card


@app.post(
    "/reviewed_cards/", response_model=ReviewedCardReadDetailed, tags=["Reviewed Cards"]
)
def create_reviewed_card(
    reviewed_card: ReviewedCardBase, db: Session = Depends(get_db)
):
    s_review_session = crud.get_review_session_by_id(
        db, reviewed_card.review_session_id
    )
    if not s_review_session:
        raise HTTPException(
            status_code=400, detail="Review Session not found. Please create it first"
        )

    return crud.create_reviewed_card(db, reviewed_card)


@app.get(
    "/review_sessions/", response_model=List[ReviewedCardRead], tags=["Review Sessions"]
)
def read_review_sessions(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    cards = crud.get_review_sessions(db, skip=skip, limit=limit)
    return cards


@app.get(
    "/review_sessions/{review_session_id}/",
    response_model=ReviewSessionReadDetailed,
    tags=["Review Sessions"],
)
def read_review_session(review_session_id: int, db: Session = Depends(get_db)):
    s_card = crud.get_review_session_by_id(db, review_session_id)
    if not s_card:
        raise HTTPException(status_code=404, detail="Reviewed Card not found")
    return s_card


@app.post(
    "/review_sessions/",
    response_model=ReviewSessionReadDetailed,
    tags=["Review Sessions"],
)
def create_review_session(
    review_session: ReviewSessionBase, db: Session = Depends(get_db)
):
    return crud.create_review_session(db, review_session)


@app.put("/review_sessions/{review_session_id}/", tags=["Review Sessions"])
def update_review_session(
    review_session_id: int,
    review_session: ReviewSessionBase,
    db: Session = Depends(get_db),
):
    s_review_session = crud.get_review_session_by_id(db, review_session_id)
    if not s_review_session:
        raise HTTPException(status_code=404, detail="Review Session not found")
    return crud.update_review_session(db, review_session, review_session_id)
