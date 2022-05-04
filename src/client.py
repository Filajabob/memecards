import discord
from discord.ext import commands
from discord.ui import Button, View

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


@client.command()
async def battle(ctx, opponent: discord.User):
    # This function does all the frontend actions such as sending battle requests, making buttons, and waiting for user
    # responses. It then delegates to utils.auto_battle() to handle battle elements.

    # Check that both parties have already started
    if not prefabs.user_exists(ctx.author.id):
        await ctx.reply("You haven't started yet. Try doing %start")
        return
    if not prefabs.user_exists(opponent.id):
        await ctx.reply(f"{opponent.mention} has not started the Meme Cards journey yet. Tell them to do %start")
        return

    request_msg = await ctx.reply(f"Sending a battle request to {opponent.mention}...")

    async def accept_callback(inter):
        await inter.response.send_message(f"Got it. Here's a magic portal to the battlefield: {ctx.channel.mention}")
        await request_msg.edit(content=f"{opponent.mention} has accepted. Good luck!")

    async def decline_callback(inter):
        await inter.response.send_message("Got it. Goodbye!")
        await request_msg.edit(content=f"{opponent.mention} declined.")

    accept = Button(label="Accept", style=discord.ButtonStyle.green)
    decline = Button(label="Decline", style=discord.ButtonStyle.red)

    accept.callback = accept_callback
    decline.callback = decline_callback

    view = View()
    view.add_item(accept)
    view.add_item(decline)

    await opponent.send(f"You have been challenged by {ctx.author.mention} to a battle! "
                        f"Click one of the options below.", view=view)

    await utils.auto_battle(ctx, ctx.author, opponent)


if __name__ == '__main__':
    client.run(Constants.TOKEN)
