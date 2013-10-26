from django.shortcuts import render

from growl.models import *
from growl.views.response import *

def bootstrap(request):

    developer = _create_developer()
    game = _create_game(developer)
    player = _create_player(game)

    response_dict = success_dict()
    response_dict['developer'] = developer
    response_dict['game'] = game
    response_dict['player'] = player

    return render_json(request, response_dict)

###
### PRIVATE
###

def _create_developer():
    developer = Developer()
    developer.email = 'a'
    developer.username = 'a'
    developer.first_name = 'a'
    developer.last_name = 'a'
    developer.password = 'a'
    developer.activated = True
    developer.save()
    return developer

def _create_game(developer):
    pass

def _create_player(game):
    pass
