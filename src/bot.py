import sys
import os
import discord
import json
import logging

from listeners.message_listener import MessageListener
import database as db

client = discord.Client()
message_listener = MessageListener()
db.create_tables()

@client.event
async def on_ready():
    print('Poggers')

@client.event
async def on_message(message):
    await message_listener.process_message(message)

with open('../.config/config.json') as f:
    data = json.load(f)

client.run(data['bot_token'])
