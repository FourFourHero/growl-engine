import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# forever
CACHE_TIMEOUT = None

def get_resource_from_cache(resource_id):
    key = _resource_cache_key(resource_id)
    resource = cache.get(key)
    if not resource:
        logger.debug('cache: resource not found: ' + resource_id)
    return resource

def store_resource_in_cache(resource):
    key = _resource_cache_key(resource.id)
    cache.set(key, resource, CACHE_TIMEOUT)
    logger.debug('cache: stored resource: ' + str(resource))

def delete_resource_from_cache(resource_id):
    key = _resource_cache_key(resource_id)
    cache.delete(key)

###
### PRIVATE
###

def _resource_cache_key(resource_id):
    return 'growl' + ':' + 'Resource:' + resource_id