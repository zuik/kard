"""
Review
- Review is a set of CardReviewed.
- Properties:
    - id: int
    - user: User that initiated the review
    - cards: List of CardReviewed (this is not in )

CardReviewed
- represented a card that was reviewed.
- contains metrics about the card during a particular review.


User owned Deck
Deck is a collection of Cards
User reviews Cards in Review
Review is a collection of CardReviewed
"""

from django.db import models

# Create your models here.

CARD_TYPE_CHOICES = [
    ("multiple_choice", "Multiple Choice"),
    ("short_answer", "Short Answer"),
]


class Deck(models.Model):
    """
    Deck: A deck holds cards
    - Name: str
    - Description: what is this deck about
    - User: User who owns the deck
        - Todo: Integrate with Django User
    - Cards: List of Cards
    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    cards = models.ManyToManyField("Card", through="CardInDeck")

    def __str__(self):
        return self.name


class Card(models.Model):
    """
    Card: A flashcard has front (prompt) and back side (answer)
    - Card type: [multiple choice, short answer]
        - Todo: multiple choice card has a list of acceptable answers and a list of potential answers
        - short answer has a str to compared for the answer
    - card's answer: For now, we only accept a str as answer.
    """

    prompt = models.TextField()
    answer = models.CharField(max_length=255)

    card_type = models.CharField(
        choices=CARD_TYPE_CHOICES,
        max_length=50,
        default="short_answer",
    )

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prompt
