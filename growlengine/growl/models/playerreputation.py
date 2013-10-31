import logging

from django.db import models
from django.db.models.signals import post_save
from growl.models.basemodel import BaseModel
from growl.caches.playerreputation import store_player_reputation_in_cache

logger = logging.getLogger(__name__)

class PlayerReputationManager(models.Manager):
    pass

class PlayerReputation(BaseModel):
    game = models.ForeignKey('Game')
    reputation = models.ForeignKey('Reputation')
    reputation_level = models.ForeignKey('ReputationLevel')
    value = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    objects = PlayerReputationManager()

    class Meta:
        db_table = 'growl_player_reputation'
        app_label = 'growl'

    def __unicode__(self):
        return self.name

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['game_id'] = self.game_id
        json['reputation_id'] = self.reputation_id
        json['reputation_level_id'] = self.reputation_level_id
        json['value_min'] = self.value_min
        json['value_max'] = self.value_max
        #json['created'] = str(self.created)
        #json['modified'] = str(self.modified)

        return json

def post_save_cache(sender, **kwargs):
    instance = kwargs.get('instance')
    store_player_reputation_in_cache(instance)
    logger.debug('post save!')

post_save.connect(post_save_cache, sender=PlayerReputation)