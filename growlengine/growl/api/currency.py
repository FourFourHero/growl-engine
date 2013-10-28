import logging
from growl.models import Currency
from growl.caches.currency import get_currency_from_cache
from growl.caches.currency import store_currency_in_cache

logger = logging.getLogger(__name__)

### Create currency
def create_currency(game, name, description, value_min, value_max):
    currency = Currency()
    currency.game = game
    currency.name = name
    currency.description = description
    currency.value_min = value_min
    currency.value_max = value_max
    currency.save() # post_save stores in cache
    return currency

### Get currency
def get_currency(currency_id):
    currency = get_currency_from_cache(currency_id)
    if not currency:
        currency = Currency.objects.get(pk=currency_id)
        store_currency_in_cache(currency)
    return currency

### Update currency
def update_currency(currency):
    currency.save() # post_save stores in cache
    return currency