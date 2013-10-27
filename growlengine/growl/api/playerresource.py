import logging
from growl.models import PlayerResource
from growl.caches.playerresource import get_player_resource_from_cache
from growl.caches.playerresource import store_player_resource_in_cache

logger = logging.getLogger(__name__)

### Create player_resource
def create_player_resource(game, player, resource, value=0):
    player_resource = PlayerResource()
    player_resource.game = game
    player_resource.player = player
    player_resource.resource = resource
    player_resource.value = value
    player_resource.save() # post_save stores in cache
    return player_resource

### Get player_resource
def get_player_resource(player_resource_id):
    player_resource = get_player_resource_from_cache(player_resource_id)
    if not player_resource:
        player_resource = PlayerResource.objects.get(pk=player_resource_id)
        store_player_resource_in_cache(player_resource)
    return player_resource

### Update player_resource
def update_player_resource(player_resource):
    player_resource.save() # post_save stores in cache
    return player_resource