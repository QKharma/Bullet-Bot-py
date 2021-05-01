from peewee import Model, CharField
from entities.base_entity import BaseEntity

class User(BaseEntity):

    discord_id = CharField(primary_key=True)
