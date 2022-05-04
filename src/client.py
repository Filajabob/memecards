import discord
from discord.ext import commands

import utils
from utils import Constants, prefabs
from classes import User, new_user, cards, load_user

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
async def stats(ctx):
    if not prefabs.user_exists(ctx.author.id):
        await ctx.reply("You haven't started yet. Try doing %start")
    else:
        user = prefabs.load_user(str(ctx.author.id))
        await ctx.send(embed=prefabs.stats(ctx.author.id))

        if not user.cards:
            return

        for card in user.cards:
            await ctx.send(embed=card.embed())


@client.command()
async def start(ctx):
    try:
        user = new_user(ctx.author.id)
    except KeyError:
        await ctx.reply("you already started you idiot")
        return

    user.add_card(cards.PythonCard(0, 100, 4, "First Card"))
    await ctx.reply("Welcome to Meme Cards! You have been gifted a Python to start you on your journey!")


if __name__ == '__main__':
    client.run(Constants.TOKEN)
