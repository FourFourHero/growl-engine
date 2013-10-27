import logging

from django.db import models
from django.db.models.signals import post_save
from growl.models.basemodel import BaseModel
from growl.caches.playerresource import store_player_resource_in_cache

logger = logging.getLogger(__name__)

class PlayerResourceManager(models.Manager):
    pass

class PlayerResource(BaseModel):
    game = models.ForeignKey('Game')
    player = models.ForeignKey('Player')
    resource = models.ForeignKey('Resource')
    value = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    objects = PlayerResourceManager()

    class Meta:
        db_table = 'growl_player_resource'
        app_label = 'growl'

    def __unicode__(self):
        return str(self.id)

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['game_id'] = self.game_id
        json['player_id'] = self.player_id
        json['resource_id'] = self.resource_id
        json['value'] = self.value
        #json['created'] = str(self.created)
        #json['modified'] = str(self.modified)

        return json

def post_save_cache(sender, **kwargs):
    instance = kwargs.get('instance')
    store_player_resource_in_cache(instance)
    logger.debug('post save!')

post_save.connect(post_save_cache, sender=PlayerResource)