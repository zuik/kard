# Generated by Django 4.0 on 2021-12-21 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('kards', '0004_deck_added_deck_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.CreateModel(
            name='ReviewSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started', models.DateTimeField(auto_now_add=True)),
                ('ended', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='CardReviewed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('correct', models.BooleanField(default=None)),
                ('time_taken', models.DurationField(default=None)),
                ('other_metrics', models.JSONField(default=None)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kards.card')),
                ('review_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kards.reviewsession')),
            ],
        ),
    ]
