from peewee import Model, SqliteDatabase
from database_init import db

class BaseEntity(Model):
    class Meta:
        database = db
