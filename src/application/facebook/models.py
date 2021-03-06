"""
This module contains the datastore models
needed for the facebook package.

.. module:: application.facebook.models

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from google.appengine.ext import db
from google.appengine.ext.db.polymodel import PolyModel

class AccessTokenModel(PolyModel):
    access_token = db.StringProperty(required=True)
    expiration = db.DateTimeProperty(required=True)

class UserAccessTokenModel(AccessTokenModel):
    username = db.StringProperty(required=True)
    user_id = db.StringProperty(required=True)
    use_albums = db.BooleanProperty(default=True)

class PageAccessTokenModel(AccessTokenModel):
    name = db.StringProperty(required=True)
    user_token = db.ReferenceProperty(UserAccessTokenModel, required=True)
    page_id = db.StringProperty(required=True)
    perms = db.StringListProperty(required=True)
    category = db.StringProperty(required=True)
    use_albums = db.BooleanProperty(default=True)

class AppAccessTokenModel(AccessTokenModel):
    name = db.StringProperty(required=True)
    user_token = db.ReferenceProperty(UserAccessTokenModel, required=True)
    category = db.StringProperty(required=True)
    app_id = db.StringProperty(required=True)

class AlbumModel(db.Model):
    token = db.ReferenceProperty(AccessTokenModel, required=True)
    me = db.StringProperty(required=True)
    name = db.StringProperty(required=True)
    desc = db.StringProperty()
    cover_photo = db.StringProperty()
    display = db.BooleanProperty(required=True, default=True)

class PhotoModel(db.Model):
    me = db.StringProperty(required=True)
    album_id = db.StringProperty(required=True)
    approved = db.BooleanProperty(required=True, default=False)
    name = db.StringProperty()
    thumbnail = db.StringProperty(required=True)
    original = db.StringProperty(required=True)