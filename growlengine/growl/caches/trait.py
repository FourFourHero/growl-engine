import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# forever
CACHE_TIMEOUT = None

def get_trait_from_cache(trait_id):
    key = _trait_cache_key(trait_id)
    trait = cache.get(key)
    if not trait:
        logger.debug('cache: trait not found: ' + trait_id)
    return trait

def store_trait_in_cache(trait):
    key = _trait_cache_key(trait.id)
    cache.set(key, trait, CACHE_TIMEOUT)
    logger.debug('cache: stored trait: ' + str(trait))

def delete_trait_from_cache(trait_id):
    key = _trait_cache_key(trait_id)
    cache.delete(key)

###
### PRIVATE
###

def _trait_cache_key(trait_id):
    return 'growl' + ':' + 'Trait:' + str(trait_id)