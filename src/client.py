import discord
from discord.ext import commands

import utils
from utils import Constants

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="mc ", intents=intents)


@client.event
async def on_ready():
    print("Ready.")


@client.command()
async def test(ctx):
    print("hi")
    await ctx.reply("hello")


if __name__ == '__main__':
    client.run(Constants.TOKEN)
