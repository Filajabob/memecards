import json
import discord
from .constants import Constants
import classes


def load_user(self, did, path=Constants.USERS_JSON):
    with open(path, 'r') as f:
        data = json.load(f)

    return classes.load_user(data[did])


def stats(did):
    did = str(did)
    user = load_user(Constants.USERS_JSON, did)
    em = discord.Embed(title="Stats")

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
