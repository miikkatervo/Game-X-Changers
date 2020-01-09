from django import forms
from gameLibrary.models import Game

class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('name', 'description', 'url', 'price',)