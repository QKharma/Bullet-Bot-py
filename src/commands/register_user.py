import discord

from entities.user import User

class RegisterUser:

    def __init__(self):
        self.UserModel = User()

    async def execute(self, message):

        author_id = message.author.id

        user_exists = self.UserModel.get_or_none(author_id)

        print(user_exists)

        if user_exists is None:
            self.UserModel.create(discord_id=author_id)
        else:
            await message.channel.send('already registered')
