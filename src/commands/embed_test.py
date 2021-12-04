import discord
import asyncio

class EmbedTest:

    alias = ['emt']

    def __init__(self, bot_client):
        self.bot_client = bot_client

    async def execute(self, message, args):

        def check_reaction(reaction, user):
            return user == message.author and str(reaction.emoji) == "<:uhoh:787702074473316383>"

        
        self.embed = discord.Embed(title='Test', description='bruh', color=0x00ff00)
        self.embed.add_field(name='field1', value='1-1-1', inline=False)
        self.embed.add_field(name='field2', value='2-2-2', inline=True)

        sent_embed = await message.channel.send(embed=self.embed)
        await sent_embed.add_reaction(":uhoh:787702074473316383")

        try:
            reaction, user = await self.bot_client.wait_for('reaction_add', timeout=60.0, check=check_reaction)
        except asyncio.TimeoutError:
            await message.channel.send('👎')
        else:
            await message.channel.send("<:uhoh:787702074473316383>")

