import logging

from django.db import models
from django.db.models.signals import post_save
from growl.models.basemodel import BaseModel
from growl.caches.skill import store_skill_in_cache

logger = logging.getLogger(__name__)

class SkillManager(models.Manager):
    pass

class Skill(BaseModel):
    game = models.ForeignKey('Game')
    name = models.CharField(max_length=256)
    description = models.TextField()
    skill_group = models.ForeignKey('SkillGroup')
    attribute_primary = models.ForeignKey('Attribute', related_name='attribute_primary_set')
    attribute_secondary = models.ForeignKey('Attribute', related_name='attribute_secondary_set')
    skill_points_cost = models.IntegerField(default=250)
    skill_points_cost_level_multiplier = models.IntegerField(default=5)
    skill_points_cost_difficulty_multiplier = models.IntegerField(default=1)
    level_max = models.IntegerField(default=5)
    skill_requirement_primary_id = models.IntegerField(default=None, null=True)
    skill_requirement_primary_level = models.IntegerField(default=None, null=True)
    skill_requirement_secondary_id = models.IntegerField(default=None, null=True)
    skill_requirement_secondary_level = models.IntegerField(default=None, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    objects = SkillManager()

    class Meta:
        db_table = 'growl_skill'
        app_label = 'growl'

    def __unicode__(self):
        return self.name

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['game_id'] = self.game_id
        json['name'] = self.name
        json['description'] = self.description
        json['skill_group_id'] = self.skill_group_id
        json['attribute_primary_id'] = self.attribute_primary_id
        json['attribute_secondary_id'] = self.attribute_secondary_id
        json['skill_points_cost'] = self.skill_points_cost
        json['skill_points_cost_level_multiplier'] = self.skill_points_cost_level_multiplier
        json['skill_points_cost_difficulty_multiplier'] = self.skill_points_cost_difficulty_multiplier
        json['level_max'] = self.level_max
        json['skill_requirement_primary_id'] = self.skill_requirement_primary_id
        json['skill_requirement_primary_level'] = self.skill_requirement_primary_level
        json['skill_requirement_secondary_id'] = self.skill_requirement_secondary_id
        json['skill_requirement_secondary_level'] = self.skill_requirement_secondary_level
        #json['created'] = str(self.created)
        #json['modified'] = str(self.modified)

        return json

        def get_skill_points_for_level(self, level):
            return int((self.skill_points_cost * self.skill_points_cost_difficulty_multiplier) * math.pow(self.skill_points_cost_level_multiplier,level-1))

        def get_level_for_skill_points(self, trained_skill_points):
            if trained_skill_points <= 0:
                return 0

            skill_level = 0
            level = 1
            while level <= self.level_max:
                skill_points_for_level = self.get_skill_points_for_level(level)
                if trained_skill_points >= skill_points_for_level:
                    skill_level = level
                level += 1

            return skill_level

def post_save_cache(sender, **kwargs):
    instance = kwargs.get('instance')
    store_skill_in_cache(instance)
    logger.debug('post save!')

post_save.connect(post_save_cache, sender=Skill)