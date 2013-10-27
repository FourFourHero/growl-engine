import logging
from growl.models import Player
from growl.caches.player import get_player_from_cache
from growl.caches.player import store_player_in_cache

logger = logging.getLogger(__name__)

### Create player
def create_player(game, client_player_id=None):
    player = Player()
    player.game = game
    if client_player_id:
        player.client_player_id = client_player_id
    player.save() # post_save stores in cache
    return player

### Get player
def get_player(player_id):
    player = get_player_from_cache(player_id)
    if not player:
        player = Player.objects.get(pk=player_id)
        store_player_in_cache(player)
    return player

### Update player
def update_player(player):
    player.save() # post_save stores in cache
    return player