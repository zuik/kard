from sqlalchemy.orm import Session
from kard.models import (
    CardBase,
    Deck,
    DeckBase,
    Card,
    ReviewSession,
    ReviewSessionBase,
    ReviewedCard,
    ReviewedCardBase,
)
from datetime import datetime, timezone
from typing import List


def get_decks(db: Session, skip: int = 0, limit: int = 100) -> List[Deck]:
    return db.query(Deck).offset(skip).limit(limit).all()


def get_deck_by_name(db: Session, name: str) -> Deck:
    return db.query(Deck).filter(Deck.name == name).first()


def get_deck_by_id(db: Session, deck_id: int) -> Deck:
    return db.query(Deck).filter(Deck.id == deck_id).first()


def create_deck(db: Session, deck: DeckBase) -> Deck:
    s_deck = Deck(
        name=deck.name,
        description=deck.description,
        added=deck.added,
        updated=deck.updated,
    )
    db.add(s_deck)
    db.commit()
    db.refresh(s_deck)
    return s_deck


def get_cards(db: Session, skip: int = 0, limit: int = 100) -> List[Card]:
    return db.query(Card).offset(skip).limit(limit).all()


def get_card_by_id(db: Session, card_id: int) -> Card:
    return db.query(Card).filter(Card.id == card_id).first()


def create_card(db: Session, card: CardBase) -> Card:
    s_card = Card(
        name=card.name,
        prompt=card.prompt,
        answer=card.answer,
        card_type=card.card_type,
        added=card.added,
        updated=card.updated,
        deck_id=card.deck_id,
    )
    db.add(s_card)
    db.commit()
    db.refresh(s_card)
    return s_card


def create_reviewed_card(db: Session, reviewed_card: ReviewedCardBase) -> ReviewedCard:
    s_reviewed_card = ReviewedCard(
        correct=reviewed_card.correct,
        time_taken=reviewed_card.time_taken,
        other_metrics=reviewed_card.other_metrics,
        card_id=reviewed_card.card_id,
        review_session_id=reviewed_card.review_session_id,
    )
    db.add(s_reviewed_card)
    db.commit()
    db.refresh(s_reviewed_card)
    return s_reviewed_card


def get_reviewed_cards(
    db: Session, skip: int = 0, limit: int = 100
) -> List[ReviewedCard]:
    return db.query(ReviewedCard).offset(skip).limit(limit).all()


def get_reviewed_card_by_id(db: Session, reviewed_card_id: int) -> ReviewedCard:
    return db.query(ReviewedCard).filter(ReviewedCard.id == reviewed_card_id).first()


def create_review_session(
    db: Session, review_session: ReviewSessionBase
) -> ReviewSession:
    s_review_session = ReviewSession(
        started=review_session.started,
        ended=review_session.ended,
        added=review_session.added,
        updated=review_session.updated,
    )

    db.add(s_review_session)
    db.commit()
    db.refresh(s_review_session)
    return s_review_session


def get_review_sessions(
    db: Session, skip: int = 0, limit: int = 100
) -> List[ReviewSession]:
    return db.query(ReviewSession).offset(skip).limit(limit).all()


def get_review_session_by_id(db: Session, review_session_id: int) -> ReviewSession:
    return db.query(ReviewSession).filter(ReviewSession.id == review_session_id).first()


def update_review_session(
    db: Session, review_session: ReviewSessionBase, review_session_id: int
) -> ReviewSession:
    db.query(ReviewSession).filter(ReviewSession.id == review_session_id).update(
        {
            "ended": review_session.ended,
            "updated": datetime.now(tz=timezone.utc),
        }
    )
    db.commit()
    s_review_session = (
        db.query(ReviewSession).filter(ReviewSession.id == review_session_id).first()
    )
    return s_review_session
