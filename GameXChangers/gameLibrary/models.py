from django.db import models

# Model User comes directly from django.contri.auth.
# https://docs.djangoproject.com/en/3.0/ref/contrib/auth/


class Game(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(default='Game Description')
    url = models.URLField(blank=True)
    highscore = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    # May be more efficient to store the "player-game" -relation
    # in the User-model. To be considered
    players = models.ManyToManyField(models.User, through='OwnedGame')
    developer = models.ForeignKey(models.User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OwnedGame(models.Model):
    player = models.ForeignKey(models.User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    bought_at = models.DateTimeField(auto_now_add=True)
    # 0-100
    progress = models.IntegerField(default=0)
    highscore = models.IntegerField(default=0)
