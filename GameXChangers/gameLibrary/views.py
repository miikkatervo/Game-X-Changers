from django.shortcuts import render
from .models import Game, OwnedGame
from django.contrib.auth.models import User
from .forms import GameForm

# Create your views here.

def home(request):
    return render(request, 'gameLibrary/home.html')

def browseGames(request):
    try:
        game_list = Game.objects.all()
        owned_game_objects = list(filter(lambda x: x.player == request.user, OwnedGame.objects.all()))
        owned_game_list = list(map(lambda x: x.game, owned_game_objects))
        context = {'game_list': game_list, 'owned_game_list': owned_game_list}
    except:
        raise Http404("Game does not exist")
    return render(request, 'gameLibrary/browseGames.html', context)

def myGames(request):
    my_games = list(filter(lambda x: x.player == request.user, OwnedGame.objects.all()))
    context = {'my_games': my_games}
    return render(request, 'gameLibrary/myGames.html', context)

# Show gaming view for specific game
def playGame(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        raise Http404("Game does not exist")
    return render(request, 'gameLibrary/playGame.html', { 'game': game })


def addGame(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.developer = request.user
            game.save()
    
    else:
        form = GameForm()

    return render(request, 'gameLibrary/addGame.html', {'form': form})
