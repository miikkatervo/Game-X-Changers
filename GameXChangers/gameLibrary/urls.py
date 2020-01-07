from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('browseGames/', views.browseGames, name='browseGames'),
    path('myGames/', views.myGames, name='myGames'),
]