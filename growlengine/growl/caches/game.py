import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# forever
CACHE_TIMEOUT = None

def get_game_from_cache(game_id):
    key = _game_cache_key(game_id)
    game = cache.get(key)
    if not game:
        logger.debug('cache: game not found: ' + str(game_id))
    return game

def store_game_in_cache(game):
    key = _game_cache_key(game.id)
    cache.set(key, game, CACHE_TIMEOUT)
    logger.debug('cache: stored game: ' + str(game))

def delete_game_from_cache(game_id):
    key = _game_cache_key(game_id)
    cache.delete(key)

###
### PRIVATE
###

def _game_cache_key(game_id):
    return 'growl' + ':' + 'Game:' + str(game_id)