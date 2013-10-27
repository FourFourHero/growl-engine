import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# forever
CACHE_TIMEOUT = None

def get_player_trait_from_cache(player_trait_id):
    key = _player_trait_cache_key(player_trait_id)
    player_trait = cache.get(key)
    if not player_trait:
        logger.debug('cache: player_trait not found: ' + player_trait_id)
    return player_trait

def store_player_trait_in_cache(player_trait):
    key = _player_trait_cache_key(player_trait.id)
    cache.set(key, player_trait, CACHE_TIMEOUT)
    logger.debug('cache: stored player_trait: ' + str(player_trait))

def delete_player_trait_from_cache(player_trait_id):
    key = _player_trait_cache_key(player_trait_id)
    cache.delete(key)

###
### PRIVATE
###

def _player_trait_cache_key(player_trait_id):
    return 'growl' + ':' + 'PlayerTrait:' + str(player_trait_id)