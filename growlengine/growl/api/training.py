import logging

from growl.api.player import get_player
from growl.api.skill import get_skill
from growl.api.playerskill import create_player_skill
from growl.api.playerskill import get_player_skill

logger = logging.getLogger(__name__)

def inject_skill(game, player, skill):

    # check for existing player skill
    player_skill = get_player_skill(player.id, skill.id)
    if player_skill:
        raise Exception('PlayerSkill already injected')

    logger.debug('creating new player skill')
    player_skill = create_player_skill(game, player, skill, level=0)
    return player_skill

def train_skill(game, player_skill):
    pass

def cancel_train_skill(game, player_skill):
    pass