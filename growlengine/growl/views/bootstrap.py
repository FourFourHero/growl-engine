import logging

from django.shortcuts import render

from growl.models import *
from growl.views.response import *
from growl.logic.attribute import roll_attribute_score

logger = logging.getLogger(__name__)

def bootstrap(request):

    developer = _create_developer()
    game = _create_game(developer)
    player = _create_player(game)
    attributes = _create_attributes(game)
    traits = _create_traits(game)
    resources = _create_resources(game)
    skill_groups = _create_skill_groups(game)
    skills = _create_skills(game, skill_groups, attributes)

    player_traits = _create_player_traits(game, player, traits)
    player_attributes = _create_player_attributes(game, player, attributes.values())
    player_resources = _create_player_resources(game, player, resources)

    response_dict = success_dict()
    response_dict['developer'] = developer
    response_dict['game'] = game
    response_dict['player'] = player
    response_dict['attributes'] = attributes
    response_dict['traits'] = traits
    response_dict['resources'] = resources
    response_dict['skill_groups'] = skill_groups
    response_dict['skills'] = skills
    response_dict['player_traits'] = player_traits
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

def _create_traits(game):
    traits = []

    trait = Trait()
    trait.game = game
    trait.name = 'Developer Access'
    trait.description = 'Sweet goodies for joining the game in its infancy'
    trait.choosable = False
    trait.effect_access_skill_group = False
    trait.access_skill_group = -1
    trait.save()
    traits.append(trait)

    return traits

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

    skill_group = SkillGroup()
    skill_group.game = game
    skill_group.name = 'Mental Prowess'
    skill_group.description = 'Mental Process desc'
    skill_group.save()
    skill_groups.append(skill_group)

    return skill_groups

def _create_skills(game, skill_groups, attributes):
    skills = []

    skill = Skill()
    skill.game = game
    skill.name = 'Legendary Perception'
    skill.description = 'Legendary Perception desc'
    skill.skill_group = skill_groups[0]
    skill.skill_points_cost_difficulty_multiplier = 1
    skill.attribute_primary = attributes['will']
    skill.attribute_secondary = attributes['per']
    skill.effect_attribute_change_per_level = True
    skill.attribute_change_per_level_value = 1
    skill.attribute_change_per_level_attribute_id = attributes['per'].id
    skill.save()
    skills.append(skill)

    return skills

def _create_player_traits(game, player, traits):
    player_traits = []

    for trait in traits:
        player_trait = PlayerTrait()
        player_trait.game = game
        player_trait.player = player
        player_trait.trait = trait
        player_trait.save()
        player_traits.append(player_trait)

    return player_traits

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