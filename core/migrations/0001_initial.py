# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Recipient'
        db.create_table(u'core_recipient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email_id', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
        ))
        db.send_create_signal(u'core', ['Recipient'])

        # Adding model 'Category'
        db.create_table(u'core_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'core', ['Category'])

        # Adding model 'Sender'
        db.create_table(u'core_sender', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('email_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Sender'])

        # Adding model 'GiftCard'
        db.create_table(u'core_giftcard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.BigIntegerField')()),
            ('expiry_date', self.gf('django.db.models.fields.DateField')()),
            ('used', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(related_name='giftcards', null=True, to=orm['core.Recipient'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='giftcards', null=True, to=orm['core.Category'])),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='giftcards', to=orm['core.Sender'])),
        ))
        db.send_create_signal(u'core', ['GiftCard'])


    def backwards(self, orm):
        # Deleting model 'Recipient'
        db.delete_table(u'core_recipient')

        # Deleting model 'Category'
        db.delete_table(u'core_category')

        # Deleting model 'Sender'
        db.delete_table(u'core_sender')

        # Deleting model 'GiftCard'
        db.delete_table(u'core_giftcard')


    models = {
        u'core.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.giftcard': {
            'Meta': {'object_name': 'GiftCard'},
            'amount': ('django.db.models.fields.BigIntegerField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'giftcards'", 'null': 'True', 'to': u"orm['core.Category']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'expiry_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'giftcards'", 'null': 'True', 'to': u"orm['core.Recipient']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'giftcards'", 'to': u"orm['core.Sender']"}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'core.recipient': {
            'Meta': {'object_name': 'Recipient'},
            'email_id': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.sender': {
            'Meta': {'object_name': 'Sender'},
            'email_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']