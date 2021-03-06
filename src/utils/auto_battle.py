import discord
from discord.ui import Button, View
import classes
from .prefabs import load_user, load_card

global c_active
global d_active

c_active = None
d_active = None

global c_attack
global d_attack

c_attack = None
d_attack = None


async def auto_battle(ctx, challenger: discord.User, defender: discord.User):
    # _challenger/_defender is the discord.User, challenger/defender is the src.classes.user.User
    # This differs from the parameter names, because I am an idiot.
    _challenger = challenger
    _defender = defender

    challenger = load_user(challenger.id)
    defender = load_user(defender.id)

    # The challengers deck of cards for the game
    cdeck = []
    # The defenders deck of cards for the game
    ddeck = []

    class SelectionButton(Button):
        def __init__(self, label: str, user: str):
            """
            A button to select your cards before a battle.

            :param label: The label of the button. Should be the name of the card.
            :param user: Indicated whether the button is for the challenger or defender. Use 'c' for challenger, and
            'd' for defender.
            """
            super().__init__(label=label)

            if user not in ('d', 'c'):
                raise ValueError("Parameter 'user' is not 'c' or 'd'")

            self.user = user

        async def callback(self, interaction):
            # For the challenger
            if self.user == 'c':
                for card in challenger.cards:
                    if card.name == self.label:
                        cdeck.append(card)
                        self.disabled = True
                        await interaction.response.send_message("Got it.")
                        break
                else:
                    raise KeyError("Card was not found.")

                # Check if the amount of cards selected for the battle is at the max (3), or all cards owned by the
                # user have been selected.
                if len(challenger.cards) == len(cdeck) or len(cdeck) >= 3:
                    self.view.stop()

            # For the defender
            else:
                for card in defender.cards:
                    if card.name == self.label:
                        ddeck.append(card)
                        self.disabled = True
                        await interaction.response.send_message("Got it.")
                        break
                else:
                    raise KeyError("Card was not found.")

                if len(defender.cards) == len(ddeck) or len(ddeck) >= 3:
                    self.view.stop()

    class CardSelectView(View):
        def __init__(self, player):
            """
            The View to select your cards before battle

            :param player: Either c or d for challenger for defender
            """
            super().__init__()

            if player == 'c':
                for card in challenger.cards:
                    button = SelectionButton(label=f"{card.name}", user=player)
                    self.add_item(button)
            else:
                for card in defender.cards:
                    button = SelectionButton(label=f"{card.name}", user=player)
                    self.add_item(button)

    cview = CardSelectView('c')
    dview = CardSelectView('d')

    await _challenger.send("Please select your cards.", view=cview)
    # Commented out for testing (quality of life)
    # await _challenger.send("Please select your cards.", view=dview)

    await cview.wait()
    # await dview.wait()

    battle = classes.Battle(challenger, defender, cdeck, ddeck)

    over = False



    while not over:
        class SelectActiveButton(Button):
            def __init__(self, label, player):
                super().__init__(label=label)
                self.label = label
                self.player = player

            async def callback(self, inter):
                if self.player == 'c':
                    for card in cdeck:
                        if card.name == self.label:
                            global c_active
                            c_active = card
                            self.view.stop()
                            break
                    else:
                        raise KeyError("Card was not found.")

                else:
                    for card in ddeck:
                        if card.name == self.label:
                            global d_active
                            d_active = card
                            self.view.stop()
                            break
                    else:
                        raise KeyError("Card was not found.")

        class SelectActiveView(View):
            def __init__(self, player):
                super().__init__()

                if player == 'c':
                    for card in cdeck:
                        button = SelectActiveButton(card.name, player)
                        self.add_item(button)
                else:
                    for card in ddeck:
                        button = SelectActiveButton(card.name, player)
                        self.add_item(button)

        class AttackSelectButton(Button):
            def __init__(self, label, player):
                super().__init__(label=label)
                self.label = label
                self.player = player

            async def callback(self, inter):
                if self.player == 'c':
                    if self.label.lower() == "primary":
                        c_attack = "primary"
                    elif self.label.lower() == "secondary":
                        c_attack = "secondary"
                    elif self.label.lower() == "special":
                        c_attack = "special"
                    else:
                        raise ValueError("Button label is not a valid attack type (primary, secondary, or special)")
                elif self.player == 'd':

                    if self.label.lower() == "primary":
                        d_attack = "primary"
                    elif self.label.lower() == "secondary":
                        d_attack = "secondary"
                    elif self.label.lower() == "special":
                        d_attack = "special"
                    else:
                        raise ValueError("Button label is not a valid attack type (primary, secondary, or special)")
                else:
                    raise ValueError("Player is not 'c' or 'd'")

        cview = SelectActiveView('c')
        dview = SelectActiveView('d')

        await ctx.send(f"{_challenger.mention}, please select your active card", view=cview)
        await cview.wait()
        # Uncomment when doing full test of battles
        # await ctx.send(f"{_defender.mention}, please select your active card", view=dview)
        # await dview.wait()

        cview = View()
        cview.add_item(AttackSelectButton("Primary", 'c'))
        cview.add_item(AttackSelectButton("Secondary", 'c'))
        cview.add_item(AttackSelectButton("Special", 'c'))

        dview = View()
        dview.add_item(AttackSelectButton("Primary", 'd'))
        dview.add_item(AttackSelectButton("Secondary", 'd'))
        dview.add_item(AttackSelectButton("Special", 'd'))

        battle.rotate(cdeck.index(c_active), ddeck.index(d_active), 'c', c_attack, d_attack)
