# -*- coding: utf-8 -*-

import datetime
from flask import url_for

from sasukekun_flask.factory import db

class Post(db.Document):
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True, unique=True)
    abstract = db.StringField()
    raw = db.StringField(required=True)
    pub_time = db.DateTimeField()
    update_time = db.DateTimeField()
    author = db.StringField()
    category = db.StringField(max_length=64)
    tags = db.ListField(db.StringField(max_length=30))


    def save(self, *args, **kw):
        now = datetime.datetime.now()
        if not self.pub_time:
            self.pub_time = now
            self.update_time = now

        return super(Post, self).save(*args, **kw)

    def to_dict(self):
        post_dict = {}

        post_dict['title'] = self.title
        post_dict['slug'] = self.slug
        post_dict['abstract'] = self.abstract
        post_dict['raw'] = self.raw
        post_dict['pub_time'] = self.pub_time
        post_dict['update_time'] = self.update_time
        post_dict['author'] = self.author
        post_dict['category'] = self.category
        post_dict['tags'] = self.tags

        return post_dict

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__

    mate = {
        'allow_inheritance': True,
        'indexes': ['slug'],
        'ordering': ['-pub_time']
    }
