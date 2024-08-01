# Generated by Django 5.0.6 on 2024-07-09 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_turn_alter_game_options_remove_game_pellet_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='number_of_turn',
        ),
        migrations.AddField(
            model_name='game',
            name='number_of_turns',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='game',
            name='turns',
            field=models.ManyToManyField(to='game.turn'),
        ),
    ]
