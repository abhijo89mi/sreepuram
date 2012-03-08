# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Settings'
        db.create_table('main_settings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site_offline', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('site_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal('main', ['Settings'])


    def backwards(self, orm):
        
        # Deleting model 'Settings'
        db.delete_table('main_settings')


    models = {
        'main.settings': {
            'Meta': {'object_name': 'Settings'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'site_offline': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['main']
