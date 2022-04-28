import discord
from discord.ext import commands

import utils
from utils import Constants
from classes import User, new_user, cards

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
    try:
        user = new_user(ctx.author.id)
    except KeyError:
        await ctx.reply("you already started you idiot")
        return

    user.cards.append(cards.PythonCard())
    await ctx.reply("Welcome to Meme Cards! You have been gifted a Python to start you on your journey!")


if __name__ == '__main__':
    client.run(Constants.TOKEN)
