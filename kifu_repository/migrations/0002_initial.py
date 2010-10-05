# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Tag'
        db.create_table('kifu_repository_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('kifu_repository', ['Tag'])

        # Adding model 'Player'
        db.create_table('kifu_repository_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('rank', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
        ))
        db.send_create_signal('kifu_repository', ['Player'])

        # Adding M2M table for field tags on 'Player'
        db.create_table('kifu_repository_player_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('player', models.ForeignKey(orm['kifu_repository.player'], null=False)),
            ('tag', models.ForeignKey(orm['kifu_repository.tag'], null=False))
        ))
        db.create_unique('kifu_repository_player_tags', ['player_id', 'tag_id'])

        # Adding model 'Kifu'
        db.create_table('kifu_repository_kifu', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sgf', self.gf('django.db.models.fields.TextField')()),
            ('player_white', self.gf('django.db.models.fields.related.ForeignKey')(related_name='player_white', to=orm['kifu_repository.Player'])),
            ('player_black', self.gf('django.db.models.fields.related.ForeignKey')(related_name='player_black', to=orm['kifu_repository.Player'])),
            ('board_size', self.gf('django.db.models.fields.PositiveIntegerField')(default=19)),
            ('handicap', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('komi', self.gf('django.db.models.fields.DecimalField')(default=6.5, max_digits=5, decimal_places=1)),
            ('rules', self.gf('django.db.models.fields.CharField')(default='Japanese', max_length=30)),
            ('result', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('event', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('visibility', self.gf('django.db.models.fields.CharField')(default='private', max_length=10)),
            ('date_recorded', self.gf('django.db.models.fields.DateField')()),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('kifu_repository', ['Kifu'])

        # Adding M2M table for field tags on 'Kifu'
        db.create_table('kifu_repository_kifu_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('kifu', models.ForeignKey(orm['kifu_repository.kifu'], null=False)),
            ('tag', models.ForeignKey(orm['kifu_repository.tag'], null=False))
        ))
        db.create_unique('kifu_repository_kifu_tags', ['kifu_id', 'tag_id'])


    def backwards(self, orm):
        
        # Deleting model 'Tag'
        db.delete_table('kifu_repository_tag')

        # Deleting model 'Player'
        db.delete_table('kifu_repository_player')

        # Removing M2M table for field tags on 'Player'
        db.delete_table('kifu_repository_player_tags')

        # Deleting model 'Kifu'
        db.delete_table('kifu_repository_kifu')

        # Removing M2M table for field tags on 'Kifu'
        db.delete_table('kifu_repository_kifu_tags')


    models = {
        'kifu_repository.kifu': {
            'Meta': {'object_name': 'Kifu'},
            'board_size': ('django.db.models.fields.PositiveIntegerField', [], {'default': '19'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {}),
            'date_recorded': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'handicap': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'komi': ('django.db.models.fields.DecimalField', [], {'default': '6.5', 'max_digits': '5', 'decimal_places': '1'}),
            'player_black': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'player_black'", 'to': "orm['kifu_repository.Player']"}),
            'player_white': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'player_white'", 'to': "orm['kifu_repository.Player']"}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rules': ('django.db.models.fields.CharField', [], {'default': "'Japanese'", 'max_length': '30'}),
            'sgf': ('django.db.models.fields.TextField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'kifus'", 'null': 'True', 'to': "orm['kifu_repository.Tag']"}),
            'visibility': ('django.db.models.fields.CharField', [], {'default': "'private'", 'max_length': '10'})
        },
        'kifu_repository.player': {
            'Meta': {'object_name': 'Player'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rank': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'players'", 'null': 'True', 'to': "orm['kifu_repository.Tag']"})
        },
        'kifu_repository.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['kifu_repository']
