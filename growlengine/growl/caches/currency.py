import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# forever
CACHE_TIMEOUT = None

def get_currency_from_cache(currency_id):
    key = _currency_cache_key(currency_id)
    currency = cache.get(key)
    if not currency:
        logger.debug('cache: currency not found: ' + str(currency_id))
    return currency

def store_currency_in_cache(currency):
    key = _currency_cache_key(currency.id)
    cache.set(key, currency, CACHE_TIMEOUT)
    logger.debug('cache: stored currency: ' + str(currency))

def delete_currency_from_cache(currency_id):
    key = _currency_cache_key(currency_id)
    cache.delete(key)

###
### PRIVATE
###

def _currency_cache_key(currency_id):
    return 'growl' + ':' + 'Currency:' + str(currency_id)