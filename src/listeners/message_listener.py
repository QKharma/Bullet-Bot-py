import sys
import os
import discord

class MessageListener:

    def __init__(self, client, prefix):
        self.prefix = prefix
        self.bot_client = client

    async def process_message(self, message):

        commands = self.bot_client.get_commands()

        if message.author.bot:
            return

        if message.content.startswith('-'):

            command = None

            command_name, *args = message.content[1:].split()

            for c_name, c_instance in commands.items():
                if c_name == command_name:
                    command = c_instance
                elif command_name in c_instance.alias:
                    command = c_instance

            if command is None:
                return
            else:
                await command.execute(message, args)
