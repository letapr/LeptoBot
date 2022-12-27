import discord
from discord.ext import commands


def random_action():
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    bot = commands.Bot(command_prefix='?', description="leptoBot", intents=intents)

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')
        print('------')

