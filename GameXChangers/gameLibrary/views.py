from django.shortcuts import render
from .models import Game, OwnedGame
from django.contrib.auth.models import User
from .forms import GameForm
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, 'gameLibrary/home.html')

def browseGames(request):

    game_list = Game.objects.all()
    owned_game_objects = list(filter(lambda x: x.player == request.user, OwnedGame.objects.all()))
    owned_game_list = list(map(lambda x: x.game, owned_game_objects))
    context = {'game_list': game_list, 'owned_game_list': owned_game_list}
    return render(request, 'gameLibrary/browseGames.html', context)

def myGames(request):
    my_games = list(filter(lambda x: x.player == request.user, OwnedGame.objects.all()))
    context = {'my_games': my_games}
    return render(request, 'gameLibrary/myGames.html', context)

# Show gaming view for specific game
def playGame(request, game_id):
    if request.method == 'GET':
        try:
            game = Game.objects.get(pk=game_id)
            owned_game_objects = list(filter(lambda x: x.game.id == game_id, OwnedGame.objects.all()))
            context = {'game': game, 'owned_game_objects': owned_game_objects,}
        except Game.DoesNotExist:
            raise Http404("Game does not exist")
    else:
        try:
            print("k")
            obj = OwnedGame.objects.filter(player=request.user)[0].game
            obj.highscore = request.POST['score']
            obj.save()
            return JsonResponse({'status':'Success', 'msg': 'save successfully'})
        except:
            raise Http404("Game not updated")
    return render(request, 'gameLibrary/playGame.html', context)


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
