from peewee import Model, CharField, IntegerField, DateField, TimeField, ForeignKeyField
from entities.base_entity import BaseEntity
from entities.user import User

class Task(BaseEntity):
    title = CharField()
    date = DateField()
    start_time = TimeField()
    end_time = TimeField()
    note = CharField()
    user = ForeignKeyField(User, backref='tasks')
