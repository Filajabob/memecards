import discord
from discord.ui import Button, View
import classes
from .prefabs import load_user


async def auto_battle(ctx, challenger: discord.User, defender: discord.User):
    class SelectionButton(Button):
        async def callback(self, interaction):
            print(self.label)

    _challenger = challenger
    _defender = defender

    cdeck = []
    ddeck = []

    view = View()

    challenger = load_user(challenger.id)
    defender = load_user(defender.id)

    for card in challenger.cards:
        # TODO: Add attribute to Card to access it's name without "Card" in it
        button = SelectionButton(label=f"{card.name}")
        view.add_item(button)

    await _challenger.send("Please select your cards.", view=view)

    battle = classes.Battle(challenger, defender, challenger.cards, defender.cards)

