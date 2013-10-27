import logging

from django.db import models
from django.db.models.signals import post_save
from growl.models.basemodel import BaseModel

logger = logging.getLogger(__name__)

class SkillGroupManager(models.Manager):
    pass

class SkillGroup(BaseModel):
    game = models.ForeignKey('Game')
    name = models.CharField(max_length=256)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    objects = SkillGroupManager()

    class Meta:
        db_table = 'growl_skill_group'
        app_label = 'growl'

    def __unicode__(self):
        return self.name

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['game_id'] = self.game_id
        json['name'] = self.name
        json['description'] = self.description
        #json['created'] = str(self.created)
        #json['modified'] = str(self.modified)

        return json

def post_save_cache(sender, **kwargs):
    instance = kwargs.get('instance')
    logger.debug('post save!')

post_save.connect(post_save_cache, sender=SkillGroup)