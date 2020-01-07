from django.shortcuts import render
from .models import Game

# Create your views here.

def home(request):
    return render(request, 'gameLibrary/home.html')

def browseGames(request):
    game_list = Game.objects.all()
    context = {'game_list': game_list}
    return render(request, 'gameLibrary/browseGames.html', context)

def myGames(request):
    return render(request, 'gameLibrary/myGames.html')

def playGame(request):
    return render(request, 'gameLibrary/playGame.html')
