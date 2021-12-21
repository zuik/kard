from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Deck, Card, CardReviewed, ReviewSession


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "url", "name"]


class DeckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deck
        fields = ["id", "url", "name", "description", "cards", "added", "updated"]


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = [
            "id",
            "url",
            "name",
            "prompt",
            "answer",
            "card_type",
            "added",
            "updated",
        ]


class CardReviewedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardReviewed
        fields = [
            "id",
            "url",
            "card",
            "review_date",
            "review_session",
            "correct",
            "time_taken",
            "other_metrics",
        ]


class ReviewSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReviewSession
        fields = ["id", "url", "user", "started", "ended", "cards_reviewed"]
