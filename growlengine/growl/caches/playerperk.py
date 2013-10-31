import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# 24 hours
CACHE_TIMEOUT = 86400

def get_player_perk_from_cache(player_perk_id):
    key = _player_perk_cache_key(player_perk_id)
    player_perk = cache.get(key)
    if not player_perk:
        logger.debug('cache: player_perk not found: ' + str(player_perk_id))
    return player_perk

def store_player_perk_in_cache(player_perk):
    key = _player_perk_cache_key(player_perk.id)
    cache.set(key, player_perk, CACHE_TIMEOUT)
    logger.debug('cache: stored player_perk: ' + str(player_perk))

def delete_player_perk_from_cache(player_perk_id):
    key = _player_perk_cache_key(player_perk_id)
    cache.delete(key)

###
### PRIVATE
###

def _player_perk_cache_key(player_perk_id):
    return 'growl' + ':' + 'PlayerPerk:' + str(player_perk_id)