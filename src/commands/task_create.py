import discord

from entities.user import User
from entities.task import Task

class TaskCreate:

    alias = ['create-task', 'ct']

    def __init__(self, bot_client):
        self.UserModel = User()
        self.TaskModel = Task()
        self.bot_client = bot_client

    async def execute(self, message, args):

        def check(m):
            return m.channel == message.channel and m.author == message.author

        await message.channel.send('task name: (c to cancel)')

        task_name = await self.bot_client.wait_for('message', check=check)

        if task_name.content == 'c':
            await message.channel.send('task creation cancelled')
            return

        await message.channel.send('date (dd.mm.yyyy):')

        task_date = await self.bot_client.wait_for('message', check=check)

        await message.channel.send('time and length (hh:mm hh:mm):')

        task_time_and_length = await self.bot_client.wait_for('message', check=check)

        await message.channel.send('note:')

        note = await self.bot_client.wait_for('message', check=check)

        await message.channel.send(f'create this task? (y/n):\n'
                                   f'name: {task_name.content}\n'
                                   f'date: {task_date.content}\n'
                                   f'time: {task_time_and_length.content}\n'
                                   f'note: {note.content}'
                                   )

        note = await self.bot_client.wait_for('message', check=check)

