import logging

from django.db import models
from django.db.models.signals import post_save
from growl.models.basemodel import BaseModel
from growl.caches.skilleffect import store_skill_effect_in_cache

logger = logging.getLogger(__name__)

class SkillEffectManager(models.Manager):
    pass

class SkillEffect(BaseModel):
    game = models.ForeignKey('Game')
    skill = models.ForeignKey('Skill')

    # effects
    effect_attribute_change_per_level = models.BooleanField(default=False)
    attribute_change_per_level_value = models.IntegerField(default=0)
    attribute_change_per_level_attribute_id = models.IntegerField(default=None, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    objects = SkillEffectManager()

    class Meta:
        db_table = 'growl_skill_effect'
        app_label = 'growl'

    def __unicode__(self):
        return str(self.id)

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['game_id'] = self.game_id
        json['skill_id'] = self.skill_id
        # effects
        json['effect_attribute_change_per_level'] = str(self.effect_attribute_change_per_level)
        json['attribute_change_per_level_value'] = self.attribute_change_per_level_value
        json['attribute_change_per_level_attribute_id'] = self.attribute_change_per_level_attribute_id
        #json['created'] = str(self.created)
        #json['modified'] = str(self.modified)

        return json

def post_save_cache(sender, **kwargs):
    instance = kwargs.get('instance')
    store_skill_effect_in_cache(instance)
    logger.debug('post save!')

post_save.connect(post_save_cache, sender=SkillEffect)