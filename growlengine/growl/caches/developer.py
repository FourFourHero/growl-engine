import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# forever
CACHE_TIMEOUT = None

def get_developer_from_cache(developer_id):
    key = _developer_cache_key(developer_id)
    developer = cache.get(key)
    if not developer:
        logger.debug('cache: developer not found: ' + developer_id)
    return developer

def store_developer_in_cache(developer):
    key = _developer_cache_key(developer.id)
    cache.set(key, developer, CACHE_TIMEOUT)
    logger.debug('cache: stored developer: ' + str(developer))

def delete_developer_from_cache(developer_id):
    key = _developer_cache_key(developer_id)
    cache.delete(key)

###
### PRIVATE
###

def _developer_cache_key(developer_id):
    return 'growl' + ':' + 'Developer:' + str(developer_id)