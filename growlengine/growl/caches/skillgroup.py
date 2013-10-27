import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# forever
CACHE_TIMEOUT = None

def get_skill_group_from_cache(skill_group_id):
    key = _skill_group_cache_key(skill_group_id)
    skill_group = cache.get(key)
    if not skill_group:
        logger.debug('cache: skill_group not found: ' + skill_group_id)
    return skill_group

def store_skill_group_in_cache(skill_group):
    key = _skill_group_cache_key(skill_group.id)
    cache.set(key, skill_group, CACHE_TIMEOUT)
    logger.debug('cache: stored skill_group: ' + str(skill_group))

def delete_skill_group_from_cache(skill_group_id):
    key = _skill_group_cache_key(skill_group_id)
    cache.delete(key)

###
### PRIVATE
###

def _skill_group_cache_key(skill_group_id):
    return 'growl' + ':' + 'SkillGroup:' + skill_group_id