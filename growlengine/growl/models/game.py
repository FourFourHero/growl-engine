import logging

from django.db import models
from django.db.models.signals import post_save
from growl.models.basemodel import BaseModel

logger = logging.getLogger(__name__)

class GameManager(models.Manager):
    pass

class Game(BaseModel):
    developer = models.ForeignKey('Developer')
    name = models.CharField(max_length=256)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    objects = GameManager()

    class Meta:
        db_table = 'growl_game'
        app_label = 'growl'

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['developer_id'] = self.developer_id
        json['name'] = self.name
        json['description'] = self.description
        json['modified'] = str(self.modified)
        json['created'] = str(self.created)
        return json

def post_save_cache(sender, **kwargs):
    logger.debug('post save!')

post_save.connect(post_save_cache, sender=Game)