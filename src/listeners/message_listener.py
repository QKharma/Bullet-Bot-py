import sys
import os
import importlib
import discord

sys.path.append(os.path.abspath('./commands'))

class MessageListener:
    def __init__(self):
        self.commands = self.load_commands()
        return

    def load_commands(self):
        command_files = os.listdir('./commands')
        command_files.remove('__pycache__')

        command_filesCleaned = []
        for item in command_files:
            command_filesCleaned.append(item[:-3])

        commands = {}

        for command_file in command_filesCleaned:
            commands[command_file] = importlib.import_module(command_file)

        return commands

    async def process_message(self, message):

        commands = self.commands

        if message.author.bot:
            return

        if message.content == 'ping':
            ping = commands['ping'].Ping()
            await ping.execute(message)

        if message.content == 'register':
            register_user = commands['register_user'].RegisterUser()
            await register_user.execute(message)
