import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# forever
CACHE_TIMEOUT = None

def get_perk_from_cache(perk_id):
    key = _perk_cache_key(perk_id)
    perk = cache.get(key)
    if not perk:
        logger.debug('cache: perk not found: ' + str(perk_id))
    return perk

def store_perk_in_cache(perk):
    key = _perk_cache_key(perk.id)
    cache.set(key, perk, CACHE_TIMEOUT)
    logger.debug('cache: stored perk: ' + str(perk))

def delete_perk_from_cache(perk_id):
    key = _perk_cache_key(perk_id)
    cache.delete(key)

###
### PRIVATE
###

def _perk_cache_key(perk_id):
    return 'growl' + ':' + 'Perk:' + str(perk_id)