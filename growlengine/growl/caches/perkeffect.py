import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# forever
CACHE_TIMEOUT = None

def get_perk_effect_from_cache(perk_effect_id):
    key = _perk_effect_cache_key(perk_effect_id)
    perk_effect = cache.get(key)
    if not perk_effect:
        logger.debug('cache: perk_effect not found: ' + str(perk_effect_id))
    return perk_effect

def store_perk_effect_in_cache(perk_effect):
    key = _perk_effect_cache_key(perk_effect.id)
    cache.set(key, perk_effect, CACHE_TIMEOUT)
    logger.debug('cache: stored perk_effect: ' + str(perk_effect))

def delete_perk_effect_from_cache(perk_effect_id):
    key = _perk_effect_cache_key(perk_effect_id)
    cache.delete(key)

###
### PRIVATE
###

def _perk_effect_cache_key(perk_effect_id):
    return 'growl' + ':' + 'PerkEffect:' + str(perk_effect_id)