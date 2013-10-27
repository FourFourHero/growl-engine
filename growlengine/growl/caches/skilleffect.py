import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# forever
CACHE_TIMEOUT = None

def get_skill_effect_from_cache(skill_effect_id):
    key = _skill_effect_cache_key(skill_effect_id)
    skill_effect = cache.get(key)
    if not skill_effect:
        logger.debug('cache: skill_effect not found: ' + skill_effect_id)
    return skill_effect

def store_skill_effect_in_cache(skill_effect):
    key = _skill_effect_cache_key(skill_effect.id)
    cache.set(key, skill_effect, CACHE_TIMEOUT)
    logger.debug('cache: stored skill_effect: ' + str(skill_effect))

def delete_skill_effect_from_cache(skill_effect_id):
    key = _skill_effect_cache_key(skill_effect_id)
    cache.delete(key)

###
### PRIVATE
###

def _skill_effect_cache_key(skill_effect_id):
    return 'growl' + ':' + 'SkillEffect:' + str(skill_effect_id)