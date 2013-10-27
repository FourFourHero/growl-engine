import logging

from django.db import models
from django.db.models.signals import post_save
from growl.models.basemodel import BaseModel
from growl.caches.trait import store_trait_in_cache

logger = logging.getLogger(__name__)

class TraitManager(models.Manager):
    pass

class Trait(BaseModel):
    game = models.ForeignKey('Game')
    name = models.CharField(max_length=256)
    description = models.TextField()
    choosable = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)

    # effects
    effect_access_skill_group = models.BooleanField(default=False)
    access_skill_group_id = models.IntegerField(default=-1)

    objects = TraitManager()

    class Meta:
        db_table = 'growl_trait'
        app_label = 'growl'

    def __unicode__(self):
        return self.name

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['game_id'] = self.game_id
        json['name'] = self.name
        json['description'] = self.description
        json['choosable'] = str(self.choosable)
        #json['created'] = str(self.created)
        #json['modified'] = str(self.modified)

        # effects
        json['effect_access_skill_group'] = str(self.effect_access_skill_group)
        json['access_skill_group_id'] = self.access_skill_group_id

        return json

def post_save_cache(sender, **kwargs):
    instance = kwargs.get('instance')
    store_trait_in_cache(instance)
    logger.debug('post save!')

post_save.connect(post_save_cache, sender=Trait)