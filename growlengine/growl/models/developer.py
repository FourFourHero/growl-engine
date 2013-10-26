from django.db import models
from growl.models import BaseModel

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
        app_label = 'growl'
        db_table = 'developer'