import json


class User:
    def __init__(self, did, xp, cards):
        self.did = did
        self.cards = cards
        self.xp = xp

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
            "cards": ser_cards
        }

        if location is not None:
            with open(location, 'r+') as f:
                data = json.load(f)
                data[self.did] = ser_user
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()

        return ser_user


def new_user(did):
    did = str(did)

    with open("../assets/text/users.json", 'r+') as f:
        users = json.load(f)

        if did in users:
            raise KeyError("User already exists.")

        user = User(did, 0, [])
        user.serialize("../assets/text/users.json")

    return user
