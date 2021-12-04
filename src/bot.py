import sys
import os
import discord
import importlib

from peewee import SqliteDatabase

from listeners.message_listener import MessageListener

import database as db

sys.path.append(os.path.abspath('./src/commands'))

class Bot:

    def __init__(self):
        self.client = discord.Client()
        self.message_listener = MessageListener(self, prefix='.')
        self.commands = self.load_commands()

    def start(self):

        db.create_tables()

        self.define_events()

        self.client.run(os.environ.get('BULLET_BOT_TOKEN'))

    def load_commands(self):

        command_files = os.listdir('./src/commands')

        try:
            command_files.remove('__pycache__')
        except ValueError:
            pass

        command_filesCleaned = []
        for item in command_files:
            command_filesCleaned.append(item[:-3])

        commands = {}

        for command_file in command_filesCleaned:

            if len(command_file.split('_')) > 1:
                class_name = command_file.split('_')[0].capitalize() + command_file.split('_')[1].capitalize()
            else:
                class_name = command_file.capitalize()

            commands[command_file] = getattr(importlib.import_module(command_file), class_name)(self.client)

        return commands

    def get_commands(self):
        return self.commands

    def define_events(self):

        @self.client.event
        async def on_ready():
            print('Poggers')

        @self.client.event
        async def on_message(message):
            await self.message_listener.process_message(message)
