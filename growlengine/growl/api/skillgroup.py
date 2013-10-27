import logging
from growl.models import SkillGroup
from growl.caches.skillgroup import get_skill_group_from_cache
from growl.caches.skillgroup import store_skill_group_in_cache

logger = logging.getLogger(__name__)

### Create skill_group
def create_skill_group(game, name, description):
    skill_group = SkillGroup()
    skill_group.game = game
    skill_group.name = name
    skill_group.description = description
    skill_group.save() # post_save stores in cache
    return skill_group

### Get skill_group
def get_skill_group(skill_group_id):
    skill_group = get_skill_group_from_cache(skill_group_id)
    if not skill_group:
        skill_group = SkillGroup.objects.get(pk=skill_group_id)
        store_skill_group_in_cache(skill_group)
    return skill_group

### Update skill_group
def update_skill_group(skill_group):
    skill_group.save() # post_save stores in cache
    return skill_group