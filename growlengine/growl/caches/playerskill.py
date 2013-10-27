import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# forever
CACHE_TIMEOUT = None

def get_player_skill_from_cache(player_skill_id):
    key = _player_skill_cache_key(player_skill_id)
    player_skill = cache.get(key)
    if not player_skill:
        logger.debug('cache: player_skill not found: ' + player_skill_id)
    return player_skill

def store_player_skill_in_cache(player_skill):
    key = _player_skill_cache_key(player_skill.id)
    cache.set(key, player_skill, CACHE_TIMEOUT)
    logger.debug('cache: stored player_skill: ' + str(player_skill))

def delete_player_skill_from_cache(player_skill_id):
    key = _player_skill_cache_key(player_skill_id)
    cache.delete(key)

###
### PRIVATE
###

def _player_skill_cache_key(player_skill_id):
    return 'growl' + ':' + 'PlayerSkill:' + str(player_skill_id)