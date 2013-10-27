# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Skill.attribute_change_per_level_value'
        db.delete_column(u'growl_skill', 'attribute_change_per_level_value')

        # Deleting field 'Skill.effect_attribute_change_per_level'
        db.delete_column(u'growl_skill', 'effect_attribute_change_per_level')

        # Deleting field 'Skill.attribute_change_per_level_attribute_id'
        db.delete_column(u'growl_skill', 'attribute_change_per_level_attribute_id')


    def backwards(self, orm):
        # Adding field 'Skill.attribute_change_per_level_value'
        db.add_column(u'growl_skill', 'attribute_change_per_level_value',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Skill.effect_attribute_change_per_level'
        db.add_column(u'growl_skill', 'effect_attribute_change_per_level',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Skill.attribute_change_per_level_attribute_id'
        db.add_column(u'growl_skill', 'attribute_change_per_level_attribute_id',
                      self.gf('django.db.models.fields.IntegerField')(default=None, null=True),
                      keep_default=False)


    models = {
        'growl.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'value_max': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'value_min': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'growl.developer': {
            'Meta': {'object_name': 'Developer'},
            'activated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'growl.game': {
            'Meta': {'object_name': 'Game'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'developer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Developer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'growl.player': {
            'Meta': {'object_name': 'Player'},
            'client_player_id': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        'growl.playerattribute': {
            'Meta': {'object_name': 'PlayerAttribute', 'db_table': "'growl_player_attribute'"},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Attribute']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Player']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
        },
        'growl.playerresource': {
            'Meta': {'object_name': 'PlayerResource', 'db_table': "'growl_player_resource'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Player']"}),
            'resource': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Resource']"})
        },
        'growl.playerskill': {
            'Meta': {'object_name': 'PlayerSkill', 'db_table': "'growl_player_skill'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'injected': ('django.db.models.fields.DateTimeField', [], {'default': 'None'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Player']"}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Skill']"}),
            'trained_skill_points': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'growl.playerskilltrainingplan': {
            'Meta': {'object_name': 'PlayerSkillTrainingPlan', 'db_table': "'growl_player_skill_training_plan'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'player_skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.PlayerSkill']"})
        },
        'growl.playertrait': {
            'Meta': {'object_name': 'PlayerTrait', 'db_table': "'growl_player_trait'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Player']"}),
            'trait': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Trait']"})
        },
        'growl.resource': {
            'Meta': {'object_name': 'Resource'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'value_max': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'value_min': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'growl.skill': {
            'Meta': {'object_name': 'Skill'},
            'attribute_primary': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attribute_primary_set'", 'to': "orm['growl.Attribute']"}),
            'attribute_secondary': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attribute_secondary_set'", 'to': "orm['growl.Attribute']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level_max': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'skill_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.SkillGroup']"}),
            'skill_points_cost': ('django.db.models.fields.IntegerField', [], {'default': '250'}),
            'skill_points_cost_difficulty_multiplier': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'skill_points_cost_level_multiplier': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'skill_requirement_primary_id': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'skill_requirement_primary_level': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'skill_requirement_secondary_id': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'skill_requirement_secondary_level': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'})
        },
        'growl.skillgroup': {
            'Meta': {'object_name': 'SkillGroup', 'db_table': "'growl_skill_group'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'growl.trait': {
            'Meta': {'object_name': 'Trait'},
            'access_skill_group_id': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'choosable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'effect_access_skill_group': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['growl']