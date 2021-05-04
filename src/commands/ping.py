import discord
from datetime import datetime

class Ping:

    alias = ['ping']

    def __init__(self, bot_client):
        self.bot_client = bot_client

    async def execute(self, message, args):

        ping_start = message.created_at

        ping_response = await message.channel.send('Pinging...')

        ping_end = ping_response.created_at

        t1 = ping_start.timestamp()
        t2 = ping_end.timestamp()

        ping_length = int((t2 - t1) * 1000)

        await ping_response.edit(content=f'Ping: {ping_length}ms')
