# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'LandingHypothesisRegistration', fields ['uuid']
        db.delete_unique('profiles_landinghypothesisregistration', ['uuid'])


        # Changing field 'LandingHypothesisRegistration.uuid'
        db.alter_column('profiles_landinghypothesisregistration', 'uuid', self.gf('uuidfield.fields.UUIDField')(max_length=36, auto=True, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'LandingHypothesisRegistration.uuid'
        raise RuntimeError("Cannot reverse this migration. 'LandingHypothesisRegistration.uuid' and its values cannot be restored.")
        # Adding unique constraint on 'LandingHypothesisRegistration', fields ['uuid']
        db.create_unique('profiles_landinghypothesisregistration', ['uuid'])


    models = {
        'profiles.landinghypothesisregistration': {
            'Meta': {'ordering': "('created',)", 'object_name': 'LandingHypothesisRegistration'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'faculty': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_student': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('uuidfield.fields.UUIDField', [], {'max_length': '36', 'auto': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['profiles']