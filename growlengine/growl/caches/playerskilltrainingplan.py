import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# 50 seconds
CACHE_TIMEOUT = 50

def get_player_skill_training_plan_from_cache(player_id):
    key = _player_skill_training_plan_cache_key(player_id)
    player_skill_training_plan = cache.get(key)
    if not player_skill_training_plan:
        logger.debug('cache: player_skill_training_plan not found: ' + str(player_id))
    return player_skill_training_plan

def store_player_skill_training_plan_in_cache(player_skill_training_plan):
    key = _player_skill_training_plan_cache_key(player_skill_training_plan.player_id)
    cache.set(key, player_skill_training_plan, CACHE_TIMEOUT)
    logger.debug('cache: stored player_skill_training_plan: ' + str(player_skill_training_plan))

def delete_player_skill_training_plan_from_cache(player_id):
    key = _player_skill_training_plan_cache_key(player_id)
    cache.delete(key)

###
### PRIVATE
###

def _player_skill_training_plan_cache_key(player_id):
    return 'growl' + ':' + 'PlayerSkillTrainingPlan:' + str(player_id)