import logging
from growl.models import PlayerCurrency
from growl.caches.playercurrency import get_player_currency_from_cache
from growl.caches.playercurrency import store_player_currency_in_cache

logger = logging.getLogger(__name__)

### Create player_currency
def create_player_currency(game, player, currency, value=None):
    player_currency = PlayerCurrency()
    player_currency.game = game
    player_currency.player = player
    player_currency.currency = currency
    if value is not None:
        player_currency.value = value
    player_currency.save() # post_save stores in cache
    return player_currency

### Get player_currency
def get_player_currency(player_id, currency_id):
    player_currency = get_player_currency_from_cache(player_id, currency_id)
    if not player_currency:
        player_currency = PlayerCurrency.objects.get(player_id=player_id, currency_id=currency_id)
        store_player_currency_in_cache(player_currency)
    return player_currency

### Update player_currency
def update_player_currency(player_currency):
    player_currency.save() # post_save stores in cache
    return player_currency