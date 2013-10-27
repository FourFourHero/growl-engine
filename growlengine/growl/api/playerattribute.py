import logging
from growl.models import PlayerAttribute
from growl.caches.playerattribute import get_player_attribute_from_cache
from growl.caches.playerattribute import store_player_attribute_in_cache

logger = logging.getLogger(__name__)

### Create player_attribute
def create_player_attribute(game, player, attribute, value=None):
    player_attribute = PlayerAttribute()
    player_attribute.game = game
    player_attribute.player = player
    player_attribute.attribute = attribute
    if value:
        player_attribute.value = value
    player_attribute.save() # post_save stores in cache
    return player_attribute

### Get player_attribute
def get_player_attribute(player_attribute_id):
    player_attribute = get_player_attribute_from_cache(player_attribute_id)
    if not player_attribute:
        player_attribute = PlayerAttribute.objects.get(pk=player_attribute_id)
        store_player_attribute_in_cache(player_attribute)
    return player_attribute

### Update player_attribute
def update_player_attribute(player_attribute):
    player_attribute.save() # post_save stores in cache
    return player_attribute