from peewee import CharField, DateField, ForeignKeyField
from entities.base_entity import BaseEntity
from entities.user import User

class Reminder(BaseEntity):
    content = CharField()
    date = DateField()
    user = ForeignKeyField(User, backref='tasks')
