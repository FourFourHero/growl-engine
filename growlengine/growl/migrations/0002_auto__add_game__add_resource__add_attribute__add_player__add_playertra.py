# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table('growl_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('developer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Developer'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('growl', ['Game'])

        # Adding model 'Resource'
        db.create_table('growl_resource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Game'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('value_min', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('value_max', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('growl', ['Resource'])

        # Adding model 'Attribute'
        db.create_table('growl_attribute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Game'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('value_min', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('value_max', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('growl', ['Attribute'])

        # Adding model 'Player'
        db.create_table('growl_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Game'])),
            ('client_player_id', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('growl', ['Player'])

        # Adding model 'PlayerTrait'
        db.create_table('growl_player_trait', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Game'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Player'])),
            ('trait', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Trait'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('growl', ['PlayerTrait'])

        # Adding model 'PlayerAttribute'
        db.create_table('growl_player_attribute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Game'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Player'])),
            ('attribute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Attribute'])),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('growl', ['PlayerAttribute'])

        # Adding model 'PlayerResource'
        db.create_table('growl_player_resource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Game'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Player'])),
            ('resource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Resource'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('growl', ['PlayerResource'])

        # Adding model 'Skill'
        db.create_table('growl_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Game'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('skill_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.SkillGroup'])),
            ('attribute_primary', self.gf('django.db.models.fields.related.ForeignKey')(related_name='attribute_primary_set', to=orm['growl.Attribute'])),
            ('attribute_secondary', self.gf('django.db.models.fields.related.ForeignKey')(related_name='attribute_secondary_set', to=orm['growl.Attribute'])),
            ('skill_points_cost', self.gf('django.db.models.fields.IntegerField')(default=250)),
            ('skill_points_cost_level_multiplier', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('skill_points_cost_difficulty_multiplier', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('level_max', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('skill_requirement_primary_id', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('skill_requirement_primary_level', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('skill_requirement_secondary_id', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('skill_requirement_secondary_level', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('effect_attribute_change_per_level', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('attribute_change_per_level_value', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('attribute_change_per_level_attribute_id', self.gf('django.db.models.fields.IntegerField')(default=-1)),
        ))
        db.send_create_signal('growl', ['Skill'])

        # Adding model 'PlayerSkillTrainingPlan'
        db.create_table('growl_player_skill_training_plan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Game'])),
            ('player_skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.PlayerSkill'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('growl', ['PlayerSkillTrainingPlan'])

        # Adding model 'PlayerSkill'
        db.create_table('growl_player_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Game'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Player'])),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Skill'])),
            ('trained_skill_points', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('injected', self.gf('django.db.models.fields.DateTimeField')(default=None)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('growl', ['PlayerSkill'])

        # Adding model 'Developer'
        db.create_table('growl_developer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('activated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('growl', ['Developer'])

        # Adding model 'Trait'
        db.create_table('growl_trait', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Game'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('choosable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('effect_access_skill_group', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('access_skill_group_id', self.gf('django.db.models.fields.IntegerField')(default=-1)),
        ))
        db.send_create_signal('growl', ['Trait'])

        # Adding model 'SkillGroup'
        db.create_table('growl_skill_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['growl.Game'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('growl', ['SkillGroup'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table('growl_game')

        # Deleting model 'Resource'
        db.delete_table('growl_resource')

        # Deleting model 'Attribute'
        db.delete_table('growl_attribute')

        # Deleting model 'Player'
        db.delete_table('growl_player')

        # Deleting model 'PlayerTrait'
        db.delete_table('growl_player_trait')

        # Deleting model 'PlayerAttribute'
        db.delete_table('growl_player_attribute')

        # Deleting model 'PlayerResource'
        db.delete_table('growl_player_resource')

        # Deleting model 'Skill'
        db.delete_table('growl_skill')

        # Deleting model 'PlayerSkillTrainingPlan'
        db.delete_table('growl_player_skill_training_plan')

        # Deleting model 'PlayerSkill'
        db.delete_table('growl_player_skill')

        # Deleting model 'Developer'
        db.delete_table('growl_developer')

        # Deleting model 'Trait'
        db.delete_table('growl_trait')

        # Deleting model 'SkillGroup'
        db.delete_table('growl_skill_group')


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
            'client_player_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
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
            'attribute_change_per_level_attribute_id': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'attribute_change_per_level_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'attribute_primary': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attribute_primary_set'", 'to': "orm['growl.Attribute']"}),
            'attribute_secondary': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attribute_secondary_set'", 'to': "orm['growl.Attribute']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'effect_attribute_change_per_level': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level_max': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'skill_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['growl.SkillGroup']"}),
            'skill_points_cost': ('django.db.models.fields.IntegerField', [], {'default': '250'}),
            'skill_points_cost_difficulty_multiplier': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'skill_points_cost_level_multiplier': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'skill_requirement_primary_id': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'skill_requirement_primary_level': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'skill_requirement_secondary_id': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'skill_requirement_secondary_level': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
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