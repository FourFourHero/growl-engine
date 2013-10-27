import logging
from growl.models import Resource
from growl.caches.resource import get_resource_from_cache
from growl.caches.resource import store_resource_in_cache

logger = logging.getLogger(__name__)

### Create resource
def create_resource(game, name, description, value_min=None, value_max=None):
    resource = Resource()
    resource.game = game
    resource.name = name
    resource.description = description
    if value_min:
        resource.value_min = value_min
    if value_max:
        resource.value_max = value_max
    resource.save() # post_save stores in cache
    return resource

### Get resource
def get_resource(resource_id):
    resource = get_resource_from_cache(resource_id)
    if not resource:
        resource = Resource.objects.get(pk=resource_id)
        store_resource_in_cache(resource)
    return resource

### Update resource
def update_resource(resource):
    resource.save() # post_save stores in cache
    return resource