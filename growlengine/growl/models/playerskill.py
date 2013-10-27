import logging

from django.db import models
from django.db.models.signals import post_save
from growl.models.basemodel import BaseModel
from growl.caches.playerskill import store_player_skill_in_cache

logger = logging.getLogger(__name__)

class PlayerSkillManager(models.Manager):
    pass

class PlayerSkill(BaseModel):
    game = models.ForeignKey('Game')
    player = models.ForeignKey('Player')
    skill = models.ForeignKey('Skill')
    trained_skill_points = models.IntegerField(default=0) # skill points trained in this skill
    level = models.IntegerField(default=-1) # level 0 once injected
    injected = models.DateTimeField(default=None) # date this skill was injected
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    objects = PlayerSkillManager()

    class Meta:
        db_table = 'growl_player_skill'
        app_label = 'growl'

    def __unicode__(self):
        return str(self.id)

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['game_id'] = self.game_id
        json['player_id'] = self.player_id
        json['skill_id'] = self.skill_id
        json['trained_skill_points'] = self.trained_skill_points
        json['level'] = self.level
        json['injected'] = str(self.injected)
        #json['created'] = str(self.created)
        #json['modified'] = str(self.modified)

        return json

def post_save_cache(sender, **kwargs):
    instance = kwargs.get('instance')
    store_player_skill_in_cache(instance)
    logger.debug('post save!')

post_save.connect(post_save_cache, sender=PlayerSkill)