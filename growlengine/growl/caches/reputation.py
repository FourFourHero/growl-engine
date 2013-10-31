import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# forever
CACHE_TIMEOUT = None

def get_reputation_from_cache(reputation_id):
    key = _reputation_cache_key(reputation_id)
    reputation = cache.get(key)
    if not reputation:
        logger.debug('cache: reputation not found: ' + str(reputation_id))
    return reputation

def store_reputation_in_cache(reputation):
    key = _reputation_cache_key(reputation.id)
    cache.set(key, reputation, CACHE_TIMEOUT)
    logger.debug('cache: stored reputation: ' + str(reputation))

def delete_reputation_from_cache(reputation_id):
    key = _reputation_cache_key(reputation_id)
    cache.delete(key)

###
### PRIVATE
###

def _reputation_cache_key(reputation_id):
    return 'growl' + ':' + 'Reputation:' + str(reputation_id)