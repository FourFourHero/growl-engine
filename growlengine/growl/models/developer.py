from django.db import models
from growl.models import BaseModel

class Developer(BaseModel):
    email = models.EmailField(max_length=254)
    username = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    password = models.TextField()
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        app_label = 'growl'
        db_table = 'developer'