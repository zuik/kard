# Generated by Django 4.0 on 2021-12-21 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kards', '0005_deck_user_reviewsession_cardreviewed'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CardReviewed',
            new_name='ReviewedCard',
        ),
    ]