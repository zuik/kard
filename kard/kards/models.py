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
from django.contrib.auth.models import User


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
    - Cards: List of Cards
    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    cards = models.ManyToManyField("Card")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    """
    Card: A flashcard has front (prompt) and back side (answer)
    - name: str: Name of the card, could be a short for prompt
    - prompt: str: The prompt to be displayed to the user
    - Card type: [multiple choice, short answer]
        - Todo: multiple choice card has a list of acceptable answers and a list of potential answers
        - short answer has a str to compared for the answer
    - answer: str: For now, we only accept a str as answer.
    """

    name = models.CharField(max_length=255)

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
        return self.name


class CardReviewed(models.Model):
    """
    CardReviewed: Log a record that a card was reviewed
    - Card: Card that was reviewed
    - Date: Date the card was reviewed
    - Correct: True if the user answered the card correctly, False otherwise, None if the user did not answer the card (skipped)
    """

    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    review_date = models.DateTimeField(auto_now_add=True)
    review_session = models.ForeignKey("ReviewSession", on_delete=models.CASCADE)

    correct = models.BooleanField(default=None)
    time_taken = models.DurationField(default=None)

    other_metrics = models.JSONField(default=None)

    def __str__(self):
        return f"{self.card} reviewed on {self.review_date}"


class ReviewSession(models.Model):
    """
    ReviewSession: A review session
    - CardReviewed: a list of CardReviewed reviewed during this session
    - User: User who initiated the review
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    started = models.DateTimeField(auto_now_add=True)
    ended = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} review session started on {self.started}"
