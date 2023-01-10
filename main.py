import os

from discord.ext import commands
import discord
from dotenv import load_dotenv
import openai

if __name__ == '__main__':
    load_dotenv()


    class MyClient(discord.Client):
        async def on_ready(self):
            print('Logged on as', self.user)

        async def on_message(self, message):
            # don't respond to ourselves
            if message.author == self.user:
                return

            if str.lower(message.content[:8]) == '@leptobot':
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=message.content[8:],
                    temperature=0.6,
                )

    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    client.run(os.environ["DISCORD_TOKEN"])

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='>', intents=intents)

    bot.run(os.environ["DISCORD_TOKEN"])

    openai.api_key = os.environ["OPENAI_API_KEY"]


