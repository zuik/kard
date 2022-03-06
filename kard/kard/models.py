from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

from datetime import datetime, timezone


from typing import Optional, List


Base = declarative_base()


class Deck(Base):
    """
    Deck: A collection of cards.

    name (str): The name of the deck.
    description (str): A description of the deck.
    added (datetime): When the deck was added.
    updated (datetime): When the deck was last updated.
    cards (List[Card]): The cards in the deck.
    """

    __tablename__ = "deck"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String, nullable=True)

    added = Column(DateTime(timezone=True), default=func.now())
    updated = Column(DateTime(timezone=True), nullable=True)

    cards = relationship("Card", back_populates="deck")

    def __repr__(self):
        return f"<Deck(id={self.id}, name={self.name})>"


class DeckBase(BaseModel):
    name: str
    description: Optional[str] = None
    added: Optional[datetime] = None
    updated: Optional[datetime] = None


class DeckRead(DeckBase):
    id: Optional[int]

    class Config:
        orm_mode = True


class DeckReadDetailed(DeckRead):
    cards: Optional[List["CardRead"]] = None

    class Config:
        orm_mode = True


class Card(Base):
    """
    Card: The card model
    id (int): The card's unique identifier
    name (str): The card's name
    prompt (str): The card's prompt. This is the str that the card shows to the user. For now, this is expected to be plain text.
    answer (str): The card's answer. This is what we will check the user's input against. For now, this is expected to be plain text.
    card_type (str): The card's type. This is used to determine how the card is presented to the user. For now, only "SHORT_ANSWER" is supported.
    added (datetime): When the card was added
    updated (datetime): When the card was last updated

    deck (Deck): The deck that the card belongs to. Cards can only belong to one deck.
    reviewed_cards (List[ReviewedCard]): The list of reviewed cards that belong to this card.
    """

    __tablename__ = "card"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    prompt = Column(String)
    answer = Column(String)
    card_type = Column(String)

    added = Column(DateTime(timezone=True), default=func.now())
    updated = Column(DateTime(timezone=True), nullable=True)

    deck = relationship("Deck", back_populates="cards")
    deck_id = Column(Integer, ForeignKey("deck.id"))

    reviewed_cards = relationship("ReviewedCard", back_populates="card")

    def __repr__(self):
        return f"<Card(id={self.id}, name={self.name})>"


class CardBase(BaseModel):
    name: str
    prompt: str
    answer: str
    card_type: str
    added: Optional[datetime] = None
    updated: Optional[datetime] = None

    deck_id: Optional[int] = None


class CardRead(CardBase):
    id: Optional[int]
    deck: Optional["DeckRead"]

    class Config:
        orm_mode = True


class CardReadDetailed(CardRead):
    deck: Optional["DeckRead"]

    class Config:
        orm_mode = True


class ReviewedCard(Base):
    """
    ReviewedCard: The reviewed card model. This is used to track every time a user reviews a card.
    id (int): The reviewed card's unique identifier
    correct (bool): Whether the user answered the card correctly. This is determined by the client.
    time_taken (float): The amount of time it took the user to answer the card. This is determined by the client.
    other_metrics (dict): Any other metrics that the client wants to track. This is determined by the client.
    added (datetime): When the reviewed card was added
    updated (datetime): When the reviewed card was last updated

    card (Card): The reviewed card. This is the card that was reviewed.
    review_session (ReviewSession): The review session that the reviewed card belongs to.
    """

    __tablename__ = "reviewed_card"

    id = Column(Integer, primary_key=True)

    correct = Column(Boolean, nullable=True)
    time_taken = Column(Float, nullable=True)
    other_metrics = Column(JSONB, nullable=True)

    added = Column(DateTime(timezone=True), default=func.now())
    updated = Column(DateTime(timezone=True), nullable=True)

    card = relationship("Card", back_populates="reviewed_cards")
    card_id = Column(Integer, ForeignKey("card.id"))

    review_session = relationship("ReviewSession", back_populates="reviewed_cards")
    review_session_id = Column(Integer, ForeignKey("review_session.id"))

    def __repr__(self):
        return f"<ReviewedCard(id={self.id}, card={self.card})>"


class ReviewedCardBase(BaseModel):
    correct: Optional[bool] = None
    time_taken: Optional[float] = None
    other_metrics: Optional[dict] = None
    added: Optional[datetime] = None
    updated: Optional[datetime] = None

    card_id: Optional[int] = None
    review_session_id: Optional[int] = None


class ReviewedCardRead(ReviewedCardBase):
    id: Optional[int]
    card: Optional["CardRead"]
    review_session: Optional["ReviewSessionRead"]

    class Config:
        orm_mode = True


class ReviewedCardReadDetailed(ReviewedCardRead):
    card: Optional["CardRead"]
    review_session: Optional["ReviewSessionRead"]

    class Config:
        orm_mode = True


class ReviewSession(Base):
    """
    ReviewSession: The review session model. This is used to track every time a user reviews a deck.
    id (int): The review session's unique identifier
    started (datetime): When the review session was started
    ended (datetime): When the review session was ended
    added (datetime): When the review session was added. The added time can be different than started time. This is for client's flexibility on tracking a review session.
    updated (datetime): When the review session was last updated.

    reviewed_cards (List[ReviewedCard]): The list of reviewed cards that belong to this review session.
    """

    __tablename__ = "review_session"

    id = Column(Integer, primary_key=True)
    started = Column(DateTime(timezone=True), nullable=True)
    ended = Column(DateTime(timezone=True), nullable=True)

    added = Column(DateTime(timezone=True), default=func.now())
    updated = Column(DateTime(timezone=True), nullable=True)

    reviewed_cards = relationship("ReviewedCard", back_populates="review_session")


class ReviewSessionBase(BaseModel):
    started: Optional[datetime] = None
    ended: Optional[datetime] = None
    added: Optional[datetime] = None
    updated: Optional[datetime] = None


class ReviewSessionRead(ReviewSessionBase):
    id: Optional[int]
    

    class Config:
        orm_mode = True


class ReviewSessionReadDetailed(ReviewSessionRead):
    reviewed_cards: List["ReviewedCardRead"]
    class Config:
        orm_mode = True


DeckReadDetailed.update_forward_refs()

CardRead.update_forward_refs()
CardReadDetailed.update_forward_refs()

ReviewedCardRead.update_forward_refs()
ReviewedCardReadDetailed.update_forward_refs()

ReviewSessionRead.update_forward_refs()
ReviewSessionReadDetailed.update_forward_refs()
