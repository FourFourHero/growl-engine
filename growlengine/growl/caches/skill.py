import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# forever
CACHE_TIMEOUT = None

def get_skill_from_cache(skill_id):
    key = _skill_cache_key(skill_id)
    skill = cache.get(key)
    if not skill:
        logger.debug('cache: skill not found: ' + str(skill_id))
    return skill

def store_skill_in_cache(skill):
    key = _skill_cache_key(skill.id)
    cache.set(key, skill, CACHE_TIMEOUT)
    logger.debug('cache: stored skill: ' + str(skill))

def delete_skill_from_cache(skill_id):
    key = _skill_cache_key(skill_id)
    cache.delete(key)

###
### PRIVATE
###

def _skill_cache_key(skill_id):
    return 'growl' + ':' + 'Skill:' + str(skill_id)