import logging

from django.db import models
from django.db.models.signals import post_save
from growl.models.basemodel import BaseModel
from growl.caches.playertrait import store_player_trait_in_cache

logger = logging.getLogger(__name__)

class PlayerTraitManager(models.Manager):
    pass

class PlayerTrait(BaseModel):
    game = models.ForeignKey('Game')
    player = models.ForeignKey('Player')
    trait = models.ForeignKey('Trait')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    objects = PlayerTraitManager()

    class Meta:
        db_table = 'growl_player_trait'
        app_label = 'growl'

    def __unicode__(self):
        return str(self.id)

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['game_id'] = self.game_id
        json['player_id'] = self.player_id
        json['trait_id'] = self.trait_id
        #json['created'] = str(self.created)
        #json['modified'] = str(self.modified)

        return json

def post_save_cache(sender, **kwargs):
    instance = kwargs.get('instance')
    store_player_trait_in_cache(instance)
    logger.debug('post save!')

post_save.connect(post_save_cache, sender=PlayerTrait)