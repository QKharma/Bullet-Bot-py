import discord

from entities.user import User

class RegisterUser:

    alias = ['register']

    def __init__(self, bot_client):
        self.UserModel = User()
        self.bot_client = bot_client

    async def execute(self, message, args):

        author_id = message.author.id

        user_exists = self.UserModel.get_or_none(author_id)

        print(user_exists)

        if user_exists is None:
            self.UserModel.create(discord_id=author_id)
        else:
            await message.channel.send('already registered')
