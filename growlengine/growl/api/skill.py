import logging
from growl.models import Skill
from growl.caches.skill import get_skill_from_cache
from growl.caches.skill import store_skill_in_cache

logger = logging.getLogger(__name__)

### Create skill
def create_skill(game, skill_group, name, description,
                 attribute_primary, attribute_secondary,
                 skill_points_cost=None,
                 skill_points_cost_level_multiplier=None,
                 skill_points_cost_difficulty_multiplier=None,
                 level_max=None,
                 skill_requirement_primary_id=None,
                 skill_requirement_primary_level=None,
                 skill_requirement_secondary_id=None,
                 skill_requirement_secondary_level=None):
    skill = Skill()
    skill.game = game
    skill.name = name
    skill.description = description
    skill.skill_group = skill_group
    skill.attribute_primary = attribute_primary
    skill.attribute_secondary = attribute_secondary
    if skill_points_cost is not None:
        skill.skill_points_cost = skill_points_cost
    if skill_points_cost_level_multiplier is not None:
        skill.skill_points_cost_level_multiplier = skill_points_cost_level_multiplier
    if skill_points_cost_difficulty_multiplier is not None:
        skill.skill_points_cost_difficulty_multiplier = skill_points_cost_difficulty_multiplier
    if level_max is not None:
        skill.level_max = level_max
    if skill_requirement_primary_id is not None:
        skill.skill_requirement_primary_id = skill_requirement_primary_id
    if skill_requirement_primary_level is not None:
        skill.skill_requirement_primary_level = skill_requirement_primary_level
    if skill_requirement_secondary_id is not None:
        skill.skill_requirement_secondary_id = skill_requirement_secondary_id
    if skill_requirement_secondary_level is not None:
        skill.skill_requirement_secondary_level = skill_requirement_secondary_level
    skill.save() # post_save stores in cache
    return skill

### Get skill
def get_skill(skill_id):
    skill = get_skill_from_cache(skill_id)
    if not skill:
        skill = Skill.objects.get(pk=skill_id)
        store_skill_in_cache(skill)
    return skill

### Update skill
def update_skill(skill):
    skill.save() # post_save stores in cache
    return skill