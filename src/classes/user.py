import json
import classes.cards as cards
import warnings


class User:
    def __init__(self, did, xp, card_deck, energy, stats):
        self.did = did
        self.cards = card_deck
        self.xp = xp
        self.energy = energy
        self.stats = stats

    def serialize(self, location=None):
        """
        Serialize the User object into a dictionary. If location is None, the final serialized object will not be saved

        Parameters:
            location (str): A JSON file.

        Returns: dict
        """

        ser_cards = []

        for card in self.cards:
            ser_cards.append(card.serialize())

        ser_user = {
            "did": self.did,
            "xp": self.xp,
            "energy": self.energy,
            "cards": ser_cards,
            "stats": self.stats
        }

        if location is not None:
            with open(location, 'r+') as f:
                data = json.load(f)
                data[self.did] = ser_user
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()

        return ser_user

    def add_card(self, card):
        if type(card).__name__ == "Card":
            warnings.warn("Loading Abstract Base Class instead of a specific species. Attacks will not work.")

        self.cards.append(card)
        self.serialize("../assets/text/users.json")


def new_user(did):
    did = str(did)

    with open("../assets/text/users.json", 'r+') as f:
        users = json.load(f)

        if did in users:
            raise KeyError("User already exists.")

        user = User(did, 0, [], 100, {
            "wins": 0,
            "losses": 0,
            "ties": 0
        })
        user.serialize("../assets/text/users.json")

    return user


def load_user(data):
    user_cards = []

    for _card in data['cards']:
        card = getattr(cards, _card['species'])
        del _card['species']

        user_cards.append(card(**_card))

    return User(data['did'], data['xp'], user_cards, data['energy'], data['stats'])

