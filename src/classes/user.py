import json


class User:
    def __init__(self):
        self.did = None
        self.cards = []
        self.xp = None

    def serialize(self, location=None):
        """
        Serialize the User object into a dictionary. If location is None, the final serialized object will not be save

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

    def new_user(self, did):
        did = str(did)

        with open("../assets/text/users.json", 'r+') as f:
            users = json.load(f)

            if did in users:
                raise KeyError("User already exists.")
            else:
                self.did = did
                self.xp = 0

        return self
