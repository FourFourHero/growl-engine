import logging
from growl.models import Perk
from growl.caches.perk import get_perk_from_cache
from growl.caches.perk import store_perk_in_cache

logger = logging.getLogger(__name__)

### Create perk
def create_perk(game, name, description, choosable=None):
    perk = Perk()
    perk.game = game
    perk.name = name
    perk.description = description
    if choosable is not None:
        perk.choosable = choosable
    perk.save() # post_save stores in cache
    return perk

### Get perk
def get_perk(perk_id):
    perk = get_perk_from_cache(perk_id)
    if not perk:
        perk = Perk.objects.get(pk=perk_id)
        store_perk_in_cache(perk)
    return perk

### Update perk
def update_perk(perk):
    perk.save() # post_save stores in cache
    return perk