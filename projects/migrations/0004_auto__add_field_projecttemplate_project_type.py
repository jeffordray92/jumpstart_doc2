# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ProjectTemplate.project_type'
        db.add_column(u'projects_projecttemplate', 'project_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['projects.ProjectType']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ProjectTemplate.project_type'
        db.delete_column(u'projects_projecttemplate', 'project_type_id')


    models = {
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project_management': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.ProjectManagement']"}),
            'project_repository': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.ProjectRepository']"}),
            'project_template': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.ProjectTemplate']"}),
            'project_test_site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.ProjectTestSite']"}),
            'project_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.ProjectType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'projects.projectmanagement': {
            'Meta': {'object_name': 'ProjectManagement'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        },
        u'projects.projectrepository': {
            'Meta': {'object_name': 'ProjectRepository'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'repo_https': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'repo_ssh': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'})
        },
        u'projects.projecttemplate': {
            'Meta': {'object_name': 'ProjectTemplate'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.ProjectType']"}),
            'repo_https': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'repo_ssh': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'projects.projecttestsite': {
            'Meta': {'object_name': 'ProjectTestSite'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        },
        u'projects.projecttype': {
            'Meta': {'object_name': 'ProjectType'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['projects']