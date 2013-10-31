import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# 24 hours
CACHE_TIMEOUT = 86400

def get_player_skill_from_cache(player_id, skill_id):
    key = _player_skill_cache_key(player_id, skill_id)
    player_skill = cache.get(key)
    if not player_skill:
        logger.debug('cache: player_skill not found: ' + key)
    return player_skill

def store_player_skill_in_cache(player_skill):
    key = _player_skill_cache_key(player_skill.player_id, player_skill.skill_id)
    cache.set(key, player_skill, CACHE_TIMEOUT)
    logger.debug('cache: stored player_skill: ' + str(player_skill))

def delete_player_skill_from_cache(player_id, skill_id):
    key = _player_skill_cache_key(player_skill)
    cache.delete(key)

###
### PRIVATE
###

def _player_skill_cache_key(player_id, skill_id):
    return 'growl' + ':' + 'PlayerSkill:' + str(player_id) + ':' + str(skill_id)