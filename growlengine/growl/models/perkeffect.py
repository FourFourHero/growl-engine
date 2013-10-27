import logging

from django.db import models
from django.db.models.signals import post_save
from growl.models.basemodel import BaseModel
from growl.caches.perkeffect import store_perk_effect_in_cache

logger = logging.getLogger(__name__)

class PerkEffectManager(models.Manager):
    pass

class PerkEffect(BaseModel):
    game = models.ForeignKey('Game')
    perk = models.ForeignKey('Perk')

    # effects
    effect_access_skill_group = models.BooleanField(default=False)
    access_skill_group_id = models.IntegerField(default=-1)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    objects = PerkEffectManager()

    class Meta:
        db_table = 'growl_perk_effect'
        app_label = 'growl'

    def __unicode__(self):
        return str(self.id)

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['game_id'] = self.game_id
        json['perk_id'] = self.perk_id
        # effects
        json['effect_access_skill_group'] = str(self.effect_access_skill_group)
        json['access_skill_group_id'] = self.access_skill_group_id
        #json['created'] = str(self.created)
        #json['modified'] = str(self.modified)

        return json

def post_save_cache(sender, **kwargs):
    instance = kwargs.get('instance')
    store_perk_effect_in_cache(instance)
    logger.debug('post save!')

post_save.connect(post_save_cache, sender=PerkEffect)