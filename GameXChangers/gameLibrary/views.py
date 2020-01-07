from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'gameLibrary/home.html')

def browseGames(request):
    return render(request, 'gameLibrary/browseGames.html')

def myGames(request):
    return render(request, 'gameLibrary/myGames.html')
