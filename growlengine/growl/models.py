from django.db import models

###
### BaseModel
###
class BaseModel(models.Model):
    pass

    class Meta:
        abstract = True

###
### Developer
###
class Developer(BaseModel):
    email = models.EmailField(unique=True, max_length=254)
    username = models.CharField(unique=True, max_length=256)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)

###
### Game
###
class Game(BaseModel):
    developer = models.ForeignKey('Developer')
    name = models.CharField(max_length=256)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)

###
### Player
###
class Player(BaseModel):
    game = models.ForeignKey('Game')
    client_player_id = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
