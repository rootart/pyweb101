# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'LandingHypothesisRegistration.first_name'
        db.alter_column('profiles_landinghypothesisregistration', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'LandingHypothesisRegistration.last_name'
        db.alter_column('profiles_landinghypothesisregistration', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'LandingHypothesisRegistration.first_name'
        raise RuntimeError("Cannot reverse this migration. 'LandingHypothesisRegistration.first_name' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'LandingHypothesisRegistration.last_name'
        raise RuntimeError("Cannot reverse this migration. 'LandingHypothesisRegistration.last_name' and its values cannot be restored.")

    models = {
        'profiles.landinghypothesisregistration': {
            'Meta': {'ordering': "('created',)", 'object_name': 'LandingHypothesisRegistration'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'faculty': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_student': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('uuidfield.fields.UUIDField', [], {'max_length': '36', 'auto': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['profiles']