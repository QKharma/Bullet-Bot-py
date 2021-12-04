from database_init import db
from entities.task import Task
from entities.user import User
from entities.reminder import Reminder

def create_tables():
    db.create_tables([User, Task, Reminder])
