# Generated by Django 5.0.6 on 2024-07-22 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0015_game_turns'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='turns',
        ),
    ]
