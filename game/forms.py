from django import forms

from game.models import Turn



class TurnForm(forms.ModelForm):
    game_id = forms.IntegerField(widget=forms.HiddenInput())
    
    class Meta:
        model = Turn
        # fields = "__all__"
        fields = ["pellet_1", "pellet_2", "pellet_3", "pellet_4",]

