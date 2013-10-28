import logging
import datetime

from celery import task
from growl.api.attribute import get_attribute
from growl.api.playerattribute import get_player_attribute
from growl.api.player import get_player
from growl.api.skill import get_skill
from growl.api.playerskill import get_player_skill
from growl.api.playerskill import update_player_skill
from growl.api.playerskilltrainingplan import get_active_player_skill_training_plans
from growl.api.playerskilltrainingplan import update_player_skill_training_plan

logger = logging.getLogger(__name__)

@task()
def task_skill_train():
    logger.debug('Training skills...')

    active_player_skill_training_plans = get_active_player_skill_training_plans()
    for player_skill_training_plan in active_player_skill_training_plans:
        logger.debug('plan for: ' + str(player_skill_training_plan.player_id))
        player_id = player_skill_training_plan.player_id
        player = get_player(player_id)
        skill_id = player_skill_training_plan.skill_id
        skill = get_skill(skill_id)

        player_skill = get_player_skill(player.id, skill.id)
        logging.debug('  player skill:' + str(player_skill))

        attribute_primary = get_attribute(skill.attribute_primary_id)
        attribute_secondary = get_attribute(skill.attribute_secondary_id)
        logging.debug('  ap: ' + attribute_primary.slug)
        logging.debug('  as: ' + attribute_secondary.slug)

        player_attribute_primary = get_player_attribute(player.id, attribute_primary.id)
        player_attribute_secondary = get_player_attribute(player.id, attribute_secondary.id)

        # TODO move to another module
        skill_points_per_minute = player_attribute_primary.value + (player_attribute_secondary.value / 2)
        logging.debug('  spm ' + str(skill_points_per_minute))

        # increment trained skill points
        logging.debug('  tsp old: ' + str(player_skill.trained_skill_points))
        player_skill.trained_skill_points += skill_points_per_minute
        logging.debug('  tsp new: ' + str(player_skill.trained_skill_points))

        current_level = player_skill.level
        next_level = current_level + 1
        skill_points_needed_for_next_level = skill.get_skill_points_for_level(next_level)
        logger.debug('  sp for next level: ' + str(skill_points_needed_for_next_level))

        if player_skill.trained_skill_points >= skill_points_needed_for_next_level:
            logging.debug('  skill leveled up!')
            # update player skill
            player_skill.trained_skill_points = skill_points_needed_for_next_level
            player_skill.level = next_level

            # update plan to not have a skill
            player_skill_training_plan.completed = datetime.datetime.now()
            update_player_skill_training_plan(player_skill_training_plan)

        # store player skill
        update_player_skill(player_skill)


    logger.debug('Skills trained!')