from django.contrib import admin

from .models import Deck, Card, ReviewedCard, ReviewSession

# Register your models here.
admin.site.register(Deck)
admin.site.register(Card)
admin.site.register(ReviewedCard)
admin.site.register(ReviewSession)
