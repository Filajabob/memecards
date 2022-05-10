import random
from .abc import Card


class PythonCard(Card):
    def bio(self):
        return {
            "backstory": "Python isn't the python he used to be, but is still feared by many. After his loss against "
                         "Apollo around 3500 BCE, Python's godly form was "
                         "destroyed and he was banished... Until now. With magic, Python is back, maybe not in his "
                         "prime form, but still a ferocious opponent nonetheless.",
            "description": "With a pretty low energy usage compared to it's attack, it's a good card for beginners. "
                           "Maybe why it's the starting card... "
        }

    def primary_attack(self):
        """
        Whip your Python's tail at the enemy with a speed feared by many.
        """

        return {
            "attack-name": "tailwhip",
            "damage": random.uniform(self.att_score * 4 - 2, self.att_score * 4 + 2),
            "energy-used": 4.5 * self.att_score  # First number is the energy factor
        }

    def secondary_attack(self):
        """
        FFFFAAAAAAAAAARRRRRRRRDDDDDDDDD
        """

        return {
            "attack-name": "fard",
            "damage": random.uniform(self.att_score * 3 - 1, self.att_score * 3 + 1),
            "energy-used": 2.75 * self.att_score
        }

    def special_attack(self):
        """
        Knock the opponent's active card out for 1 rotation
        """

        return {
            "attack-name": "venom",
            "damage": random.uniform(self.att_score * 10 - 1, self.att_score * 10 + 1),
            "energy-used": 20 * self.att_score,
            "action": "knockout"
        }


class SpiderCard(Card):
    def bio(self):
        return {
            "backstory": "",
            "description": ""
        }

    def primary_attack(self):
        """
        Eight legs of strangling power jumping on you is kinda terrifying.
        """
        return {
            "attack-name": "pounce",
            "damage": random.uniform(self.att_score * 7 - 1, self.att_score * 7 + 1),
            "energy-used": 24 * self.att_score,
        }

    def secondary_attack(self):
        """
        Who said a spider couldn't kick?
        """

        return {
            "attack-name": "kick",
            "damage": random.uniform(self.att_score * 2 - 1, self.att_score * 2 + 1),
            "energy-used": 15 * self.att_score
        }

    def special_attack(self):
        """
        Webs. Cool.
        """

        return {
            "attack-name": "web-attack",
            "damage": random.uniform(self.att_score * 19 - 1, self.att_score * 19 + 1),
            "energy-used": 32 * self.att_score,
            "action": "knockout"
        }


class GoatCard(Card):
    def bio(self):
        return {
            "backstory": "He's the goat"
        }

    def primary_attack(self):
        """
        Have you ever been rammed by a goat? No? Would you like to?
        """

        return {
            "attack-name": "ram",
            "damage": random.uniform(self.att_score * 13 - 1, self.att_score * 13 + 1),
            "energy-used": 135
        }

    def secondary_attack(self):
        """
        Damn he got better kicks then Messi.
        """

        return {
            "attack-name": "hind-kick",
            "damage": random.uniform(self.att_score * 5 - 1, self.att_score * 5 + 1),
            "energy-used": 50
        }

    def special_attack(self):
        """
        Sometimes emotional damage is more painful than a punch
        """

        return {
            "attack-name": "disrespect",
            "damage": random.uniform(self.att_score * 25 - 1, self.att_score * 25 + 1),
            "energy-used": 150
        }


class StevensDadCard(Card):

    def bio(self):
        return {
            "backstory": "He went to school both ways on one foot (allegedly), the other was starting a business"
                         " (Beijing Corn). He moved to America where he had Steven, also known as 'Failure'."
        }

    def primary_attack(self):
        """
        Nothing beats the slipper. Oh god I'm getting traumatic flashbacks already.
        """

        return {
            "attack-name": "slipper",
            "damage": random.uniform(self.att_score * 8 - 1, self.att_score * 8 + 1),
            "energy-used": 65
        }

    def secondary_attack(self):
        """
        When I was your age I ...
        """

        return {
            "attack-name": "when-i-was-your-age-i",
            "damage": random.uniform(self.att_score * 3 - 1, self.att_score * 3 + 1),
            "energy-used": 40
        }

    def special_attack(self):
        """
        *inhales* EEEEEEEEEEEEMOOOOOOOOOOOTTTTTTTTTTTIIOOOOOOOOOOOOOONNNNNNNNNAAAAAAAAAAALLLLLLLLLLLLL DAAAAAAAAAAAAAAMA
        AAAAAAAGGGGEEEE
        """

        return {
            "attack-name": "emotional-damage",
            "damage": random.uniform(self.att_score * 30 - 1, self.att_score * 30 + 1),
            "energy-used": 165
        }


class KnightCard(Card):

    def bio(self):
        return {
            "backstory": "He trained hard as a kid to get here. He's a ferocious fighter to all his enemies."

        }

    def primary_attack(self):
        """
        Its more painful than it looks (and it looks very painful)
        """

        return {
            "attack-name": "swipe",
            "damage": random.uniform(self.att_score * 6 - 1, self.att_score * 6 + 1),
            "energy-used": 80

        }

    def secondary_attack(self):
        """
        This is kinda lame tbh
        """

        return {
            "attack-name": "knife",
            "damage": random.uniform(self.att_score * 5 - 1, self.att_score * 5 + 1),
            "energy-used": 45
        }

    def special_attack(self):
        """
        Wow he can run pretty quick saying that knight armor is very heavy.
        """

        return {
            "attack-name": "charge",
            "damage": random.uniform(self.att_score * 12 - 1, self.att_score * 12 + 1),
            "energy-used": 120
        }


class GorillaCard(Card):
    def bio(self):
        return {
            "backstory": "The Gorilla came from the forests as a peaceful guy, until one unfortunate day his home was "
                         "destroyed. Now he is here to fight and avenge the loss of his home."

        }

    def primary_attack(self):
        """
        Better than any football player I've ever seen.
        """

        return {
            "attack-name": "tackle",
            "damage": random.uniform(self.att_score * 8 - 1, self.att_score * 8 + 1),
            "energy-used": 85
        }

    def secondary_attack(self):
        """
        Well he is a twelve time GFC champion
        """

        return {
            "attack-name": "punch",
            "damage": random.uniform(self.att_score * 5 - 1, self.att_score * 5 + 1),
            "energy-used": 35
        }

    def special_attack(self):
        """
        This makes endless street fighter combos look lame
        """

        return {
            "attack-name": "combos",
            "damage": random.uniform(self.att_score * 6 - 1, self.att_score * 6 + 1),
            "energy-used": 0
        }


class SorceressCard(Card):
    def bio(self):
        return {
            "backstory": "A very feared witch that has mastered the arts of magic from 21 years of experience."
        }

    def primary_attack(self):
        """
        That just looks painful...
        """

        return {
            "attack-name": "posion-spell",
            "damage": random.uniform(self.att_score * 5 - 1, self.att_score * 5 + 1),
            "energy-used": 70
        }

    def secondary_attack(self):
        """
        Why would you do that if you are a literal witch- nevermind.
        """

        return {
            "attack-name": "staff",
            "damage": random.uniform(self.att_score * 4 - 1, self.att_score * 4 + 1),
            "energy-used": 60
        }

    def special_attack(self):
        """
        oOoOoOoh creepy curse
        """

        return {
            "attack-name": "curse",
            "damage": random.uniform(self.att_score * 26 - 1, self.att_score * 26 + 1),
            "energy-used": 150
        }



