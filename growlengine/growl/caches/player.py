import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# forever
CACHE_TIMEOUT = None

def get_player_from_cache(player_id):
    key = _player_cache_key(player_id)
    player = cache.get(key)
    if not player:
        logger.debug('cache: player not found: ' + player_id)
    return player

def store_player_in_cache(player):
    key = _player_cache_key(player.id)
    cache.set(key, player, CACHE_TIMEOUT)
    logger.debug('cache: stored player: ' + str(player))

def delete_player_from_cache(player_id):
    key = _player_cache_key(player_id)
    cache.delete(key)

###
### PRIVATE
###

def _player_cache_key(player_id):
    return 'growl' + ':' + 'Player:' + str(player_id)