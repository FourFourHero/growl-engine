from django.db import models
from growl.models.basemodel import BaseModel

class Game(BaseModel):
    developer = models.ForeignKey('Developer')
    name = models.CharField(max_length=256)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)

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