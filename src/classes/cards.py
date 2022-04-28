import random
from .abc import Card


class PythonCard(Card):
    def primary_attack(self):
        """
        Whip your Python's tail at the enemy with a speed feared by many.
        """

        return {
            "attack-name": "tailwhip",
            "damage": random.uniform(self.att_score * 7 - 2, self.att_score * 7 + 2),
            "energy-used": 60
        }

    def secondary_attack(self):
        """
        FFFFAAAAAAAAAARRRRRRRRDDDDDDDDD
        """

        return {
            "attack-name": "fard",
            "damage": random.uniform(self.att_score * 6 - 1, self.att_score * 6 + 1),
            "energy-used": 50
        }

    def special_attack(self):
        """
        Knock the opponent's active card out for 1 rotation
        """

        return {
            "attack-name": "venom",
            "damage": random.uniform(self.att_score * 10 - 1, self.att_score * 10 + 1),
            "energy-used": 100,
            "action": "knockout"
        }


class SpiderCard(Card):
    def primary_attack(self):
        """
        Eight legs of strangling power jumping on you is kinda terrifying.
        """
        return {
            "attack-name": "pounce",
            "damage": random.uniform(self.att_score * 7 - 1, self.att_score * 7 + 1),
            "energy-used": 120,
        }

    def secondary_attack(self):
        """
        Who said a spider couldn't kick?
        """

        return {
            "attack-name": "kick",
            "damage": random.uniform(self.att_score * 2 - 1, self.att_score * 2 + 1)
            "energy-used": 75
        }
