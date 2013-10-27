import logging
from growl.models import PlayerPerk
from growl.caches.playerperk import get_player_perk_from_cache
from growl.caches.playerperk import store_player_perk_in_cache

logger = logging.getLogger(__name__)

### Create player_perk
def create_player_perk(game, player, perk):
    player_perk = PlayerPerk()
    player_perk.game = game
    player_perk.player = player
    player_perk.perk = perk
    player_perk.save() # post_save stores in cache
    return player_perk

### Get player_perk
def get_player_perk(player_perk_id):
    player_perk = get_player_perk_from_cache(player_perk_id)
    if not player_perk:
        player_perk = PlayerPerk.objects.get(pk=player_perk_id)
        store_player_perk_in_cache(player_perk)
    return player_perk

### Update player_perk
def update_player_perk(player_perk):
    player_perk.save() # post_save stores in cache
    return player_perk