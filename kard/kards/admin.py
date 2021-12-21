from django.contrib import admin

from .models import Deck, Card, CardReviewed, ReviewSession

# Register your models here.
admin.site.register(Deck)
admin.site.register(Card)
admin.site.register(CardReviewed)
admin.site.register(ReviewSession)
