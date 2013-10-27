from django.shortcuts import render

from growl.models import *
from growl.views.response import *
from growl.logic.attribute import roll_attribute_score

def bootstrap(request):

    developer = _create_developer()
    game = _create_game(developer)
    player = _create_player(game)
    attributes = _create_attributes(game)
    player_attributes = _create_player_attributes(game, player, attributes.values())

    response_dict = success_dict()
    response_dict['developer'] = developer
    response_dict['game'] = game
    response_dict['player'] = player
    response_dict['attributes'] = attributes
    response_dict['player_attributes'] = player_attributes

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
    game = Game()
    game.developer = developer
    game.name = 'Game name'
    game.description = 'Game desc'
    game.save()
    return game

def _create_player(game):
    player = Player()
    player.game = game

    player.save()
    return player

def _create_attributes(game):
    attributes = {}

    attr = Attribute()
    attr.game = game
    attr.slug = 'mem'
    attr.name = 'Memory'
    attr.description = 'Memory desc'
    attr.save()
    attributes['mem'] = attr

    attr = Attribute()
    attr.game = game
    attr.slug = 'pres'
    attr.name = 'Presence'
    attr.description = 'Presence desc'
    attr.save()
    attributes['pres'] = attr

    attr = Attribute()
    attr.game = game
    attr.slug = 'init'
    attr.name = 'Initiative'
    attr.description = 'Initiative desc'
    attr.save()
    attributes['init'] = attr

    attr = Attribute()
    attr.game = game
    attr.slug = 'per'
    attr.name = 'Perception'
    attr.description = 'Perception desc'
    attr.save()
    attributes['per'] = attr

    attr = Attribute()
    attr.game = game
    attr.slug = 'int'
    attr.name = 'Intelligence'
    attr.description = 'Intelligence desc'
    attr.save()
    attributes['int'] = attr

    attr = Attribute()
    attr.game = game
    attr.slug = 'will'
    attr.name = 'Willpower'
    attr.description = 'Willpower desc'
    attr.save()
    attributes['will'] = attr

    return attributes

def _create_player_attributes(game, player, attributes):
    player_attributes = []

    for attribute in attributes:
        player_attribute = PlayerAttribute()
        player_attribute.game = game
        player_attribute.player = player
        player_attribute.attribute = attribute
        player_attribute.value = roll_attribute_score(player)
        player_attribute.save()
        player_attributes.append(player_attribute)

    return player_attributes