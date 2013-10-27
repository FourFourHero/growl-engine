import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# forever
CACHE_TIMEOUT = None

def get_attribute_from_cache(attribute_id):
    key = _attribute_cache_key(attribute_id)
    attribute = cache.get(key)
    if not attribute:
        logger.debug('cache: attribute not found: ' + attribute_id)
    return attribute

def store_attribute_in_cache(attribute):
    key = _attribute_cache_key(attribute.id)
    cache.set(key, attribute, CACHE_TIMEOUT)
    logger.debug('cache: stored attribute: ' + str(attribute))

def delete_attribute_from_cache(attribute_id):
    key = _attribute_cache_key(attribute_id)
    cache.delete(key)

###
### PRIVATE
###

def _attribute_cache_key(attribute_id):
    return 'growl' + ':' + 'Attribute:' + str(attribute_id)