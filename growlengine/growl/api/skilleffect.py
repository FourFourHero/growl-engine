import logging
from growl.models import SkillEffect
from growl.caches.skilleffect import get_skill_effect_from_cache
from growl.caches.skilleffect import store_skill_effect_in_cache

logger = logging.getLogger(__name__)

### Create skill_effect
def create_skill_effect(game, skill,
                        effect_attribute_change_per_level=None,
                        attribute_change_per_level_value=None,
                        attribute_change_per_level_attribute_id=None):
    skill_effect = SkillEffect()
    skill_effect.game = game
    skill_effect.skill = skill
    if effect_attribute_change_per_level:
        skill_effect.effect_attribute_change_per_level = effect_attribute_change_per_level
    if attribute_change_per_level_value
        skill_effect.attribute_change_per_level_value = attribute_change_per_level_value
    if attribute_change_per_level_attribute_id:
        skill_effect.attribute_change_per_level_attribute_id = attribute_change_per_level_attribute_id
    skill_effect.save() # post_save stores in cache
    return skill_effect

### Get skill_effect
def get_skill_effect(skill_effect_id):
    skill_effect = get_skill_effect_from_cache(skill_effect_id)
    if not skill_effect:
        skill_effect = SkillEffect.objects.get(pk=skill_effect_id)
        store_skill_effect_in_cache(skill_effect)
    return skill_effect

### Update skill_effect
def update_skill_effect(skill_effect):
    skill_effect.save() # post_save stores in cache
    return skill_effect