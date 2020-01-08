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

# Show gaming view for specific game
def playGame(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'gameLibrary/playGame.html', { 'game': game })
