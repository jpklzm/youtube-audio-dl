# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'YouTube'
        db.create_table(u'api_youtube', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('video_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('duration', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('audio_filename', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('audio_filesize', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('download_count', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('last_download_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal(u'api', ['YouTube'])

        # Adding model 'ActivityLog'
        db.create_table(u'api_activitylog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('client_ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('video_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'api', ['ActivityLog'])


    def backwards(self, orm):
        # Deleting model 'YouTube'
        db.delete_table(u'api_youtube')

        # Deleting model 'ActivityLog'
        db.delete_table(u'api_activitylog')


    models = {
        u'api.activitylog': {
            'Meta': {'object_name': 'ActivityLog'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'client_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'api.youtube': {
            'Meta': {'object_name': 'YouTube'},
            'audio_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'audio_filesize': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'download_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'duration': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_download_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'video_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['api']