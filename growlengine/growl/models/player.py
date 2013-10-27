import logging

from django.db import models
from django.db.models.signals import post_save
from growl.models.basemodel import BaseModel

logger = logging.getLogger(__name__)

class PlayerManager(models.Manager):
    pass

class Player(BaseModel):
    game = models.ForeignKey('Game')
    client_player_id = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    objects = PlayerManager()

    class Meta:
        db_table = 'growl_player'
        app_label = 'growl'

    def __unicode__(self):
        return str(self.id)

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['game_id'] = self.game_id
        json['client_player_id'] = self.client_player_id
        #json['created'] = str(self.created)
        #json['modified'] = str(self.modified)

        return json

def post_save_cache(sender, **kwargs):
    instance = kwargs.get('instance')
    logger.debug('post save!')

post_save.connect(post_save_cache, sender=Player)