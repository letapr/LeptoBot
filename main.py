import os

from discord.ext import commands
import discord
from dotenv import load_dotenv

from lepto import random_action

if __name__ == '__main__':
    load_dotenv()

    class MyClient(discord.Client):
        async def on_ready(self):
            print('Logged on as', self.user)

        async def on_message(self, message):
            # don't respond to ourselves
            if message.author == self.user:
                return

            if message.content == 'ping':
                await message.channel.send('pong')


    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    client.run(os.environ["DISCORD_TOKEN"])


    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='>', intents=intents)


    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')


    bot.run(os.environ["DISCORD_TOKEN"])
