class Card:
    def __init__(self, xp=None, hp=None, att_score=None, name="Generic Card"):
        """
        To load a card from a JSON file, use Python's **kwargs utility.

        :param xp: Shorthand for experience
        :param hp: Shorthand for hitpoints. Hitpoints is the amount of damage you can take until "dying"
        :param att_score: A score that is relative to how many attacks the card has done.
        """
        self.xp = xp
        self.hp = hp
        self.att_score = att_score
        self.name = name

        if not xp is None:
            self.level = xp // 100

            if self.level > 100:
                self.level = 100

            if self.level <= 19:
                self.rarity = "common"
            elif 20 <= self.level <= 39:
                self.rarity = "uncommon"
            elif 40 <= self.level <= 59:
                self.rarity = "rare"
            elif 60 <= self.level <= 79:
                self.rarity = "epic"
            else:
                self.rarity = "meme"

        else:
            self.level = None
            self.rarity = None

    def primary_attack(self):
        pass

    def secondary_attack(self):
        pass

    def special_attack(self):
        pass

    def serialize(self):
        """
        Convert a card's data to a JSON compatible format.
        :return: dict
        """

        return {
            "xp": self.xp,
            "hp": self.hp,
            "att_score": self.att_score,
            "species": type(self).__name__
        }

    def bio(self):
        pass

