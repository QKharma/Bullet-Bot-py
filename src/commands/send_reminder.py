import discord
import time
from discord.ext import tasks, commands

class SendReminder:

    alias = ['send-reminder', 'sr']

    def __init__(self, bot_client):
        self.bot_client = bot_client
        self.threads = {}

    async def execute(self, message, args):

        self.message = message
        self.args = args

        if self.args == []:
            await message.channel.send("```missing argument: send-reminder <start|stop>```")
        else:
            if self.args[0] == 'start':
                self.start_reminder()
            elif self.args[0] == 'stop':
                self.stop_reminder()

    def start_reminder(self):

        self.threads[self.message.author.id] = Reminder(self.message)
        self.threads[self.message.author.id].reminder.start()

    def stop_reminder(self):

        self.threads[self.message.author.id].reminder.cancel()

class Reminder():

    def __init__(self, message):
        self.message = message

    @tasks.loop(seconds=10)
    async def reminder(self):

        if True:
            if not self.message.author.dm_channel:
                await self.message.author.create_dm()

            await self.message.author.dm_channel.send("blablabla")
