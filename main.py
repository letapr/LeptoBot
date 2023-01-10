import os

from discord.ext import commands
import discord
from dotenv import load_dotenv
import openai

if __name__ == '__main__':
    load_dotenv()
    openai.api_key = os.environ["OPENAI_API_KEY"]


    class MyClient(discord.Client):
        async def on_ready(self):
            print('Logged on as', self.user)

        async def on_message(self, message):
            print("received: " + message.content)
            if message.author == self.user:
                return

            if str.lower(message.content[:23]) == "<@&1056746274109530116>":
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=message.content[8:],
                    temperature=0.6,
                )
                print("sending: " + response.choices[0].text)
                await message.channel.send(response.choices[0].text)


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
