import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# 24 hours
CACHE_TIMEOUT = 86400

def get_player_currency_from_cache(player_id, currency_id):
    key = _player_currency_cache_key(player_id, currency_id)
    player_currency = cache.get(key)
    if not player_currency:
        logger.debug('cache: player_currency not found: ' + key)
    return player_currency

def store_player_currency_in_cache(player_currency):
    key = _player_currency_cache_key(player_currency.player_id, player_currency.currency_id)
    cache.set(key, player_currency, CACHE_TIMEOUT)
    logger.debug('cache: stored player_currency: ' + str(player_currency))

def delete_player_currency_from_cache(player_id, currency_id):
    key = _player_currency_cache_key(player_id, currency_id)
    cache.delete(key)

###
### PRIVATE
###

def _player_currency_cache_key(player_id, currency_id):
    return 'growl' + ':' + 'PlayerCurrency:' + str(player_id) + ':' + str(currency_id)