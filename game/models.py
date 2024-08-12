from django.db import models
from django.contrib.auth.models import User

SQUARE_LIST = [("Jaune",f"{chr(0x1F7E8)}"),
               ("Bleue", f"{chr(0x1F7E6)}"),
               ("Rouge", f"{chr(0x1F7E5)}"),
               ("Vert", f"{chr(0x1F7E9)}"),
               ("Violet", f"{chr(0x1F7EA)}"),
               ("Marron", f"{chr(0x1F7EB)}"),
               ]

class Turn(models.Model):
    pellet_1 = models.CharField(max_length=6, choices=SQUARE_LIST)
    pellet_2 = models.CharField(max_length=6, choices=SQUARE_LIST)
    pellet_3 = models.CharField(max_length=6, choices=SQUARE_LIST)
    pellet_4 = models.CharField(max_length=6, choices=SQUARE_LIST)

class Game(models.Model):
    winning_combination = models.CharField(max_length=100)
    number_of_turns = models.IntegerField(default=10)
    end_game = models.BooleanField(default=False)
    msg_end_game = models.TextField(default="", null=True, blank=True)
    turns = models.TextField(default="", null=True, blank=True)

    def __str__(self) -> str:
        return "Partie en cours"
    
    class Meta:
        verbose_name = "Partie"