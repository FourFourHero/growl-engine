import logging

from django.shortcuts import render

from growl.models import *
from growl.views.response import *
from growl.logic.attribute import roll_attribute_score
from growl.api.game import create_game
from growl.api.player import create_player
from growl.api.attribute import create_attribute
from growl.api.perk import create_perk
from growl.api.perkeffect import create_perk_effect
from growl.api.skill import create_skill
from growl.api.skillgroup import create_skill_group

logger = logging.getLogger(__name__)

def bootstrap(request):
    developer = _create_developer()
    game = _create_game(developer)
    player = _create_player(game)
    attributes = _create_attributes(game)
    perks = _create_perks(game)
    resources = _create_resources(game)
    skill_groups = _create_skill_groups(game)
    skills = _create_skills(game, skill_groups, attributes)

    player_perks = _create_player_perks(game, player, perks)
    player_attributes = _create_player_attributes(game, player, attributes.values())
    player_resources = _create_player_resources(game, player, resources)

    response_dict = success_dict()
    response_dict['developer'] = developer
    response_dict['game'] = game
    response_dict['player'] = player
    response_dict['attributes'] = attributes
    response_dict['perks'] = perks
    response_dict['resources'] = resources
    response_dict['skill_groups'] = skill_groups
    response_dict['skills'] = skills
    response_dict['player_perks'] = player_perks
    response_dict['player_attributes'] = player_attributes
    response_dict['player_resources'] = player_resources

    return render_json(request, response_dict)

###
### PRIVATE
###

def _create_developer():
    developer = Developer()
    developer.email = 'andrew@fourfourhero.com'
    developer.username = 'aschulak'
    developer.first_name = 'Andrew'
    developer.last_name = 'Schulak'
    developer.password = 'password'
    developer.activated = True
    developer.save()
    return developer

def _create_game(developer):
    game = create_game(developer, 'Game name', 'Game desc')
    return game

def _create_player(game):
    player = create_player(game)
    return player

def _create_attributes(game):
    attributes = {}

    attr = create_attribute(game, 'Memory', 'mem', 'Memory desc', 3, 18)
    attributes['mem'] = attr

    attr = create_attribute(game, 'Presence', 'pres', 'Presence desc', 3, 18)
    attributes['pres'] = attr

    attr = create_attribute(game, 'Initiative', 'init', 'Initiative desc', 3, 18)
    attributes['init'] = attr

    attr = create_attribute(game, 'Perception', 'per', 'Perception desc', 3, 18)
    attributes['per'] = attr

    attr = create_attribute(game, 'Intelligence', 'int', 'Intelligence desc', 3, 18)
    attributes['int'] = attr

    attr = create_attribute(game, 'Willpower', 'will', 'Willpower desc', 3, 18)
    attributes['will'] = attr

    return attributes

def _create_perks(game):
    perks = []

    perk = create_perk(game, 'Developer Access','Sweet goodies for joining the game in its infancy', choosable=False)
    perk_effect = create_perk_effect(game, perk)
    perk.perk_effect = perk_effect
    perks.append(perk)

    return perks

def _create_resources(game):
    resources = []

    resource = Resource()
    resource.game = game
    resource.name = 'Prestige'
    resource.description = 'Widespread respect and admiration felt for someone or something on the basis of a perception of their achievements or quality.'
    resource.save()
    resources.append(resource)

    return resources

def _create_skill_groups(game):
    skill_groups = []

    skill_group = create_skill_group(game, 'Mental Prowess', 'Mental Process desc')
    skill_groups.append(skill_group)

    return skill_groups

def _create_skills(game, skill_groups, attributes):
    skills = []

    skill = create_skill(game, skill_groups[0], 'Legendary Perception',
        'Legendary Perception desc', attributes['will'], attributes['per'])
    skills.append(skill)

    return skills

def _create_player_perks(game, player, perks):
    player_perks = []

    for perk in perks:
        player_perk = PlayerPerk()
        player_perk.game = game
        player_perk.player = player
        player_perk.perk = perk
        player_perk.save()
        player_perks.append(player_perk)

    return player_perks

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

def _create_player_resources(game, player, resources):
    player_resources = []

    for resource in resources:
        player_resource = PlayerResource()
        player_resource.game = game
        player_resource.player = player
        player_resource.resource = resource
        player_resource.save()
        player_resources.append(player_resource)

    return player_resources