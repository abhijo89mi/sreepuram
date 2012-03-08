# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('gallery_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('category_description', self.gf('django.db.models.fields.TextField')()),
            ('category_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('category_image', self.gf('sreepuram.widgets.RemovableImageField')(max_length=100, null=True, blank=True)),
            ('is_publish', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('gallery', ['Category'])

        # Adding model 'CategoryImage'
        db.create_table('gallery_categoryimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('image_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Category'], to_field='category_name')),
            ('image', self.gf('sreepuram.widgets.RemovableImageField')(max_length=100, null=True, blank=True)),
            ('image_description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('is_publish', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('gallery', ['CategoryImage'])

        # Adding model 'ContactUs'
        db.create_table('gallery_contactus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 3, 4, 23, 48, 6, 165963))),
        ))
        db.send_create_signal('gallery', ['ContactUs'])


    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('gallery_category')

        # Deleting model 'CategoryImage'
        db.delete_table('gallery_categoryimage')

        # Deleting model 'ContactUs'
        db.delete_table('gallery_contactus')


    models = {
        'gallery.category': {
            'Meta': {'ordering': "['id']", 'object_name': 'Category'},
            'category_description': ('django.db.models.fields.TextField', [], {}),
            'category_image': ('sreepuram.widgets.RemovableImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'category_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_publish': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        'gallery.categoryimage': {
            'Meta': {'ordering': "['order']", 'object_name': 'CategoryImage'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sreepuram.widgets.RemovableImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Category']", 'to_field': "'category_name'"}),
            'image_description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'is_publish': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        'gallery.contactus': {
            'Meta': {'ordering': "['publish_date']", 'object_name': 'ContactUs'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 3, 4, 23, 48, 6, 165963)'})
        }
    }

    complete_apps = ['gallery']
