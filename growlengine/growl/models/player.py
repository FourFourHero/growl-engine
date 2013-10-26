from django.db import models
from growl.models.basemodel import BaseModel

class Player(BaseModel):
    game = models.ForeignKey('Game')
    client_player_id = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        db_table = 'growl_player'
        app_label = 'growl'