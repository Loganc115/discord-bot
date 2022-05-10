import discord

import Token
from Token import token


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        messageContent = message.content
        if len(messageContent) > 0:
            if message.content.startswith('$hello'):
                await message.channel.send(
                    f"trollin {message.mentions[0].name}"
                )
client = MyClient()




client.run(Token.token)