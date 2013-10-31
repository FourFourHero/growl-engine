import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# forever
CACHE_TIMEOUT = None

def get_reputation_level_from_cache(reputation_level_id):
    key = _reputation_level_cache_key(reputation_level_id)
    reputation_level = cache.get(key)
    if not reputation_level:
        logger.debug('cache: reputation_level not found: ' + str(reputation_level_id))
    return reputation_level

def store_reputation_level_in_cache(reputation_level):
    key = _reputation_level_cache_key(reputation_level.id)
    cache.set(key, reputation_level, CACHE_TIMEOUT)
    logger.debug('cache: stored reputation_level: ' + str(reputation_level))

def delete_reputation_level_from_cache(reputation_level_id):
    key = _reputation_level_cache_key(reputation_level_id)
    cache.delete(key)

###
### PRIVATE
###

def _reputation_level_cache_key(reputation_level_id):
    return 'growl' + ':' + 'ReputationLevel:' + str(reputation_level_id)