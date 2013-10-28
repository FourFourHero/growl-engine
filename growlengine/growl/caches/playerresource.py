import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# forever
CACHE_TIMEOUT = None

def get_player_resource_from_cache(player_resource_id):
    key = _player_resource_cache_key(player_resource_id)
    player_resource = cache.get(key)
    if not player_resource:
        logger.debug('cache: player_resource not found: ' + str(player_resource_id))
    return player_resource

def store_player_resource_in_cache(player_resource):
    key = _player_resource_cache_key(player_resource.id)
    cache.set(key, player_resource, CACHE_TIMEOUT)
    logger.debug('cache: stored player_resource: ' + str(player_resource))

def delete_player_resource_from_cache(player_resource_id):
    key = _player_resource_cache_key(player_resource_id)
    cache.delete(key)

###
### PRIVATE
###

def _player_resource_cache_key(player_resource_id):
    return 'growl' + ':' + 'PlayerResource:' + str(player_resource_id)