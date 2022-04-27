import discord
from discord.ext import commands

import utils
from utils import Constants
from classes import User

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="%", intents=intents)


@client.event
async def on_ready():
    print("Ready.")


@client.command()
async def test(ctx):
    print("hi")
    await ctx.reply("hello")


@client.command()
async def start(ctx):
    User.new_user()


if __name__ == '__main__':
    client.run(Constants.TOKEN)
