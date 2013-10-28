import logging

from django.db import models
from django.db.models.signals import post_save
from growl.models.basemodel import BaseModel
from growl.caches.playercurrency import store_player_currency_in_cache

logger = logging.getLogger(__name__)

class PlayerCurrencyManager(models.Manager):
    pass

class PlayerCurrency(BaseModel):
    game = models.ForeignKey('Game')
    player = models.ForeignKey('Player')
    currency = models.ForeignKey('Currency')
    value = models.IntegerField(default=-1)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    objects = PlayerCurrencyManager()

    class Meta:
        db_table = 'growl_player_currency'
        app_label = 'growl'

    def __unicode__(self):
        return str(self.id)

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['game_id'] = self.game_id
        json['player_id'] = self.player_id
        json['currency_id'] = self.currency_id
        json['value'] = self.value
        #json['created'] = str(self.created)
        #json['modified'] = str(self.modified)

        return json

def post_save_cache(sender, **kwargs):
    instance = kwargs.get('instance')
    store_player_currency_in_cache(instance)
    logger.debug('post save!')

post_save.connect(post_save_cache, sender=PlayerCurrency)