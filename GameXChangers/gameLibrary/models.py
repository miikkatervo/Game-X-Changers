from django.db import models
from django.db.models import Model



# Model User comes directly from django.contri.auth
# with username as unique attribute
 

class Game(models.Model):
    name = models.CharField(max_length=30 , unique = True)
    players = models.ManyToManyField(
        User, 
        through = 'OwnedGame',
        through_fields = ('game', 'user'),
    )
    description = models.TextField
    url = models.URLField
    highscore = models.IntegerField
    price = models.IntegerField
    

class Transaction(models.Model):
    buyerName = models.CharField(max_length=30 , unique = True)
    description = models.TextField
    price = models.IntegerField
    timestamp = models.DateTimeField(auto_now_add=True)

#progress and highscore are as attributes because if they are as models with foreignKeys, we'd have to iterate 3 times when working
#with a specific user/game pair.
class OwnedGame(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    game = models.ForeignKey(Game, on_delete = models.CASCADE)
    #0-100
    progress = models.IntegerField
    highscore = models.IntegerField

#only one developer per game, thus game is unique
class DevelopedGame(models.Model):
    user = models.CharField(max_length=30 )
    game = models.CharField(max_length=30 , unique = True)
