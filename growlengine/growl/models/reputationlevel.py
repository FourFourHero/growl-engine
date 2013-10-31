import logging

from django.db import models
from django.db.models.signals import post_save
from growl.models.basemodel import BaseModel
from growl.caches.reputationlevel import store_reputation_level_in_cache

logger = logging.getLogger(__name__)

class ReputationLevelManager(models.Manager):
    pass

class ReputationLevel(BaseModel):
    game = models.ForeignKey('Game')
    reputation = models.ForeignKey('Reputation')
    name = models.CharField(max_length=256)
    description = models.TextField(null=True)
    level = models.IntegerField() # positive for good standing, negative for bad standing
    value_min = models.IntegerField() # reputation value this level starts at, one more than value_max of level lower
    value_max = models.IntegerField() # rep value this level ends at,
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    objects = ReputationLevelManager()

    class Meta:
        db_table = 'growl_reputation_level'
        app_label = 'growl'

    def __unicode__(self):
        return self.name

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['game_id'] = self.game_id
        json['reputation_id'] = self.reputation_id
        json['name'] = self.name
        json['description'] = self.description
        json['value_min'] = self.value_min
        json['value_max'] = self.value_max
        #json['created'] = str(self.created)
        #json['modified'] = str(self.modified)

        return json

def post_save_cache(sender, **kwargs):
    instance = kwargs.get('instance')
    store_reputation_level_in_cache(instance)
    logger.debug('post save!')

post_save.connect(post_save_cache, sender=ReputationLevel)