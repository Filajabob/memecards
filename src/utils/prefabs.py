import json
import discord
from .constants import Constants
import classes


def load_user(did, path=Constants.USERS_JSON):
    did = str(did)

    with open(path, 'r') as f:
        data = json.load(f)

    return classes.load_user(data[did])


def load_card(species, json_file, did, name):
    """
    Quick and easy way to load a card from a JSON file.

    :param species: The species, including "Card" at the end
    :param json_file: The JSON file being loaded from
    :param did: The Discord ID of the user
    :param name: The custom name of the card
    :return: src.classes.abc.Card
    """
    with open(json_file, 'r') as f:
        data = json.load(f)

    return getattr(classes.cards, species)(**data[str(did)][name])


def stats(did, color=discord.Color.dark_blue()):
    did = str(did)
    user = load_user(did, Constants.USERS_JSON)
    em = discord.Embed(title="Stats", color=color)

    # Start with win/loss stats
    em.add_field(name="Wins", value=user.stats["wins"])
    em.add_field(name="Losses", value=user.stats["losses"])
    em.add_field(name="Ties", value=user.stats["ties"])

    if user.stats["losses"] != 0:
        em.add_field(name="Win/Loss Ratio", value=user.stats["wins"] / user.stats["losses"])
    else:
        em.add_field(name="Win/Loss Ratio", value="0")

    return em


def user_exists(did):
    with open(Constants.USERS_JSON, 'r') as f:
        data = json.load(f)

    return str(did) in data
