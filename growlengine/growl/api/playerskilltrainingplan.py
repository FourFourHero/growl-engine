import logging
import datetime
from django.core.exceptions import ObjectDoesNotExist

from growl.models import PlayerSkillTrainingPlan
from growl.caches.playerskilltrainingplan import get_player_skill_training_plan_from_cache
from growl.caches.playerskilltrainingplan import store_player_skill_training_plan_in_cache

logger = logging.getLogger(__name__)

### Create player_skill_training_plan
def create_player_skill_training_plan(game, player, skill):
    player_skill_training_plan = PlayerSkillTrainingPlan()
    player_skill_training_plan.game = game
    player_skill_training_plan.player = player
    player_skill_training_plan.skill = skill
    player_skill_training_plan.save() # post_save stores in cache
    return player_skill_training_plan

### Get player_skill_training_plan
def get_player_skill_training_plan(player_id):
    player_skill_training_plan = get_player_skill_training_plan_from_cache(player_id)
    if not player_skill_training_plan:
        try:
            player_skill_training_plan = PlayerSkillTrainingPlan.objects.get(player_id=player_id)
        except ObjectDoesNotExist:
            pass
        else:
            store_player_skill_training_plan_in_cache(player_skill_training_plan)
    return player_skill_training_plan

### Update player_skill_training_plan
def update_player_skill_training_plan(player_skill_training_plan):
    player_skill_training_plan.save() # post_save stores in cache
    return player_skill_training_plan

### Get all active
def get_all_active_player_skill_training_plans():
    # TODO cache
    active_player_skill_training_plans = PlayerSkillTrainingPlan.objects.filter(completed=None)
    return active_player_skill_training_plans