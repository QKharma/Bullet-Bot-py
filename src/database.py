from database_init import db
from entities.task import Task
from entities.user import User

def create_tables():
    db.create_tables([User, Task])
