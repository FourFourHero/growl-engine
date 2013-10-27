import logging
from growl.models import PerkEffect
from growl.caches.perkeffect import get_perk_effect_from_cache
from growl.caches.perkeffect import store_perk_effect_in_cache

logger = logging.getLogger(__name__)

### Create perk_effect
def create_perk_effect(game, perk, effect_access_skill_group=None,
                       access_skill_group_id=None):
    perk_effect = PerkEffect()
    perk_effect.game = game
    perk_effect.perk = perk
    if effect_access_skill_group is not None:
        perk_effect.effect_access_skill_group = effect_access_skill_group
    if access_skill_group_id is not None:
        perk_effect.access_skill_group_id = access_skill_group_id
    perk_effect.save() # post_save stores in cache
    return perk_effect

### Get perk_effect
def get_perk_effect(perk_effect_id):
    perk_effect = get_perk_effect_from_cache(perk_effect_id)
    if not perk_effect:
        perk_effect = PerkEffect.objects.get(pk=perk_effect_id)
        store_perk_effect_in_cache(perk_effect)
    return perk_effect

### Update perk_effect
def update_perk_effect(perk_effect):
    perk_effect.save() # post_save stores in cache
    return perk_effect