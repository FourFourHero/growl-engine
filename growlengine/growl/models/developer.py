from django.db import models
from growl.models.basemodel import BaseModel

class Developer(BaseModel):
    email = models.EmailField(unique=True, max_length=254)
    username = models.CharField(unique=True, max_length=256)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)

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