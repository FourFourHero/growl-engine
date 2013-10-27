import logging
from growl.models import PlayerSkill
from growl.caches.playerskill import get_player_skill_from_cache
from growl.caches.playerskill import store_player_skill_in_cache

logger = logging.getLogger(__name__)

### Create player_skill
def create_player_skill(game, player, skill,
                        trained_skill_points=None, level=None):
    player_skill = PlayerSkill()
    player_skill.game = game
    player_skill.player = player
    player_skill.skill = skill
    if trained_skill_points:
        player_skill.trained_skill_points = trained_skill_points
    if level:
        player_skill.level = level
    player_skill.save() # post_save stores in cache
    return player_skill

### Get player_skill
def get_player_skill(player_skill_id):
    player_skill = get_player_skill_from_cache(player_skill_id)
    if not player_skill:
        player_skill = PlayerSkill.objects.get(pk=player_skill_id)
        store_player_skill_in_cache(player_skill)
    return player_skill

### Update player_skill
def update_player_skill(player_skill):
    player_skill.save() # post_save stores in cache
    return player_skill