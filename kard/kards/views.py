from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import (
    UserSerializer,
    GroupSerializer,
    DeckSerializer,
    CardSerializer,
    ReviewedCardSerializer,
    ReviewSessionSerializer,
)
from .models import Deck, Card, ReviewedCard, ReviewSession


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeckViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Deck to be viewed or edited.
    """

    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [permissions.IsAuthenticated]


class CardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Card to be viewed or edited.
    """

    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReviewedCardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ReviewedCard to be viewed or edited.
    """

    queryset = ReviewedCard.objects.all()
    serializer_class = ReviewedCardSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReviewSessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ReviewSession to be viewed or edited.
    """

    queryset = ReviewSession.objects.all()
    serializer_class = ReviewSessionSerializer
    permission_classes = [permissions.IsAuthenticated]
