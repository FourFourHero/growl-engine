import logging

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from growl.models.basemodel import BaseModel

logger = logging.getLogger(__name__)

class DeveloperManager(models.Manager):
    pass

class Developer(BaseModel):
    # TODO make unique
    #email = models.EmailField(unique=True, max_length=254)
    #username = models.CharField(unique=True, max_length=256)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    objects = DeveloperManager()

    class Meta:
        db_table = 'growl_developer'
        app_label = 'growl'

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['email'] = self.email
        json['username'] = self.username
        json['first_name'] = self.first_name
        json['last_name'] = self.last_name
        json['activated'] = str(self.activated)
        #json['created'] = str(self.created)
        #json['modified'] = str(self.modified)

        return json

def post_save_cache(sender, **kwargs):
    logger.debug('post save!')

post_save.connect(post_save_cache, sender=Developer)