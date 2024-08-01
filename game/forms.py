from django import forms

from game.models import Turn



class TurnForm(forms.ModelForm):
    
    class Meta:
        model = Turn
        fields = ["pellet_1", "pellet_2", "pellet_3", "pellet_4",]

