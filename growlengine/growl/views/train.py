import logging

from growl.views.response import *
from growl.api.game import *
from growl.api.player import *
from growl.api.skill import *
from growl.api.training import inject_skill

logger = logging.getLogger(__name__)

def train_inject_skill(request):
    game_id = request.GET['game_id']
    player_id = request.GET['player_id']
    skill_id = request.GET['skill_id']

    game = get_game(game_id)
    player = get_player(player_id)
    skill = get_skill(skill_id)
    
    logger.debug('game ' + str(game))
    logger.debug('player ' + str(player))
    logger.debug('skill ' + str(skill))

    player_skill = inject_skill(game, player, skill)

    response_dict = success_dict()
    response_dict['player_skill'] = player_skill

    return render_json(request, response_dict)