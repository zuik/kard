# Generated by Django 4.0 on 2021-12-21 05:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kards', '0003_alter_card_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deck',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]