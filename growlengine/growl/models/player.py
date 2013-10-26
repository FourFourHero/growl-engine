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

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['game_id'] = self.game_id
        json['client_player_id'] = self.client_player_id
        #json['created'] = str(self.created)
        #json['modified'] = str(self.modified)

        return json