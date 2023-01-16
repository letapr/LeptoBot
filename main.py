import os
from typing import Any

from discord import Intents
from discord.ext import commands
import discord
from dotenv import load_dotenv
import openai

if __name__ == '__main__':
    load_dotenv()
    openai.api_key = os.environ["OPENAI_API_KEY"]


    class MyClient(discord.Client):
        def __init__(self, *, intents: Intents, **options: Any):
            super().__init__(intents=intents, **options)
            self.id = None

        async def on_ready(self):
            print('Logged on as', self.user.mention)

        async def on_message(self, message):
            print("received: " + message.content)
            if message.author == self.user:
                return

            print(message.content[:23] + " " + self.user.mention)
            if message.content[0] == '<':
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=message.content[23:],
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
    intents.members = True
    bot = commands.Bot(command_prefix='>', intents=intents)


    @client.event
    async def on_message(message):
        if client.user.mentioned_in(message):
            print(message.content[:23] + " " )
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=message.content[23:],
                temperature=0.6,
            )

            print("sending: " + response.choices[0].text)
            await message.channel.send(response.choices[0].text)


    bot.run(os.environ["DISCORD_TOKEN"])
