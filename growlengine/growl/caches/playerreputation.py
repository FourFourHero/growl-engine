import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# 24 hours
CACHE_TIMEOUT = 86400

def get_player_reputation_from_cache(player_reputation_id):
    key = _player_reputation_cache_key(player_reputation_id)
    player_reputation = cache.get(key)
    if not player_reputation:
        logger.debug('cache: player_reputation not found: ' + str(player_reputation_id))
    return player_reputation

def store_player_reputation_in_cache(player_reputation):
    key = _player_reputation_cache_key(player_reputation.id)
    cache.set(key, player_reputation, CACHE_TIMEOUT)
    logger.debug('cache: stored player_reputation: ' + str(player_reputation))

def delete_player_reputation_from_cache(player_reputation_id):
    key = _player_reputation_cache_key(player_reputation_id)
    cache.delete(key)

###
### PRIVATE
###

def _player_reputation_cache_key(player_reputation_id):
    return 'growl' + ':' + 'PlayerReputation:' + str(player_reputation_id)