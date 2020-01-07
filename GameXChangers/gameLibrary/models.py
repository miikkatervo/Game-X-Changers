from django.db import models
from django.db.models import Model



# Model User comes directly from django.contri.auth
# with username as unique attribute
 

class Game(models.Model):
    name = models.CharField(max_length=30 , unique = True)
    description = models.TextField(default='Game Description')
    url = models.URLField(blank=True)
    highscore = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    buyerName = models.CharField(max_length=30 , unique = True)
    description = models.TextField
    price = models.IntegerField
    timestamp = models.DateTimeField(auto_now_add=True)

class OwnedGame(models.Model):
    user = models.CharField(max_length=30)
    game = models.CharField(max_length=30)
    #0-100
    progress = models.IntegerField
    highscore = models.IntegerField

#only one developer per game, thus game is unique
class DevelopedGame(models.Model):
    user = models.CharField(max_length=30 )
    game = models.CharField(max_length=30 , unique = True)
