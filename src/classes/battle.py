from .errors import BattleEnded
import random


class Battle:
    def __init__(self, challenger, defender, cdeck, ddeck, save_results=True):
        if not len(cdeck) <= 3 or not len(ddeck) <= 3:
            raise ValueError("Active deck cannot contain more than 3 cards.")
        elif len(cdeck) == 0 == len(ddeck):
            raise ValueError("Decks must have at least one card each.")

        self.d_active = None
        self.c_active = None

        self.ddeck = ddeck
        self.cdeck = cdeck

        # Amount of XP that should be rewarded after the battle
        self.c_xp = 0
        self.d_xp = 0

        # Amount of Attack Score that should be rewarded after the battle
        self.c_att_score = 0
        self.d_att_score = 0

        # Amount of HP that should be rewarded AFTER the battle
        self.c_hp = 0
        self.d_hp = 0

        self.attack = None
        self.d_attack = None
        self.c_attack = None

        self.challenger = challenger
        self.defender = defender
        self.winner = None

        self.rotation_num = 1

    def rotate(self, c_active, d_active, attacker, c_attack, d_attack):
        """
        Rotate to the next rotation.
        This function does NOT update stats automatically. However, it does return how much of each stat should be
        updated when the battle ends. (When self.winner is not None)

        :param c_active: The active card index of the challenger.
        :param d_active: The active card index of the defender.
        :param attacker: A char representing which person is attacking. For challenger, input 'c', for defender,
        input 'd'.
        :param c_attack: The attack done by the challenger. For primary attack, input "primary", etc.
        :param d_attack: Same as above, except the attacker is the defender.
        :return: dict
        """

        if self.winner:
            raise BattleEnded("Battle has already ended")

        self.c_active = self.cdeck[c_active]
        self.d_active = self.ddeck[d_active]

        for i in range(0, 2):
            if attacker == 'c':
                if c_attack == "primary":
                    self.attack = self.c_active.primary_attack()
                    self.c_att_score += round(random.uniform(0.3, 0.7), 2)
                    self.c_xp += random.randint(2, 4)

                    self.d_hp += random.randint(2, 4)
                elif c_attack == "secondary":
                    self.attack = self.c_active.secondary_attack()
                    self.c_att_score += round(random.uniform(0.1, 0.5), 2)
                    self.c_xp += random.randint(1, 2)

                    self.d_hp += random.randint(1, 2)
                elif c_attack == "special":
                    self.attack = self.c_active.special_attack()
                    self.c_att_score += round(random.uniform(1, 1.5), 2)
                    self.c_xp += random.randint(5, 9)

                    self.d_hp += random.randint(4, 7)

                self.c_attack = self.attack
                self.challenger.energy -= self.attack['energy-used']
                self.d_active.hp -= round(self.attack['damage'], 2)

            elif attacker == 'd':
                if d_attack == "primary":
                    self.attack = self.d_active.primary_attack()
                    self.d_att_score += round(random.uniform(0.3, 0.7), 2)
                    self.d_xp += random.randint(2, 4)

                    self.c_hp += random.randint(2, 4)
                elif d_attack == "secondary":
                    self.attack = self.d_active.secondary_attack()
                    self.d_att_score += round(random.uniform(0.1, 0.5), 2)
                    self.d_xp += random.randint(1, 2)

                    self.c_hp += random.randint(1, 2)
                elif d_attack == "special":
                    self.attack = self.d_active.special_attack()
                    self.d_att_score += round(random.uniform(1, 1.5), 2)
                    self.d_xp += random.randint(5, 9)

                    self.c_hp += random.randint(4, 7)

                self.d_attack = self.attack
                self.defender.energy -= self.attack['energy-used']
                self.c_active.hp -= self.attack['damage']
            else:
                raise ValueError(f"Unknown attacker {attacker}, please refer to classes.Battle.rotate.__doc__")

            if self.d_active.hp <= 0:
                # self.defender.hp = None
                self.ddeck.pop(d_active)

            if self.c_active.hp <= 0:
                # self.challenger.hp = None
                self.cdeck.pop(c_active)

            # Too lazy to make it so you can't "go into debt" for energy, maybe will add later

            # Battle End Condition 1: Challenger has 0 or less energy, or has no cards remaining, and the defender
            # still has 1 or more energy and still has (a) card(s). Winner: Defender
            if (self.challenger.energy <= 0 or len(self.cdeck) == 0) and not (
                    self.defender.energy <= 0 or len(self.ddeck) == 0):
                self.winner = "defender"
                self.d_xp += 20

                # Without this line, it would appear that the challenger attacked before dying, and the attack
                # information would be identical to the challenger's previous attack.
                self.c_attack = {}
                break

            # Battle End Condition 2: Same as above, but reversed (replace challenger with defender, and vice versa).
            # Winner: Challenger
            elif not (self.challenger.energy <= 0 or len(self.cdeck) == 0) and (
                    self.defender.energy <= 0 or len(self.ddeck) == 0):
                self.winner = "challenger"
                self.c_xp += 20

                # Without this line, it would appear that the defender attacked before dying, and the attack
                # information would be identical to the defender's previous attack.
                self.d_attack = {}

                break

            # Battle End Condition 3: Both parties have run out of energy, or have no cards. Winner: None (tie)
            elif (self.challenger.energy <= 0 or len(self.cdeck) == 0) and (
                    self.defender.energy <= 0 or len(self.cdeck) == 0):
                self.winner = "tie"

                self.d_attack = {}
                self.c_attack = {}

                break

            # Make sure the other side gets a turn
            if attacker == 'c':
                attacker = 'd'
            else:
                attacker = 'c'

        self.rotation_num += 1

        if self.winner is not None:
            return {
                "challenger_attack": self.c_attack,
                "defender_attack": self.d_attack,
                "winner": self.winner,
                "energy": {
                    "challenger": self.challenger.energy,
                    "defender": self.defender.energy
                },
                "hp": {
                    "challenger": self.c_active.hp,
                    "defender": self.d_active.hp
                },
                "decks": {
                    "challenger": self.cdeck,
                    "defender": self.ddeck
                }
            }
        else:
            # This return statement should be identical to the above except for stat updates
            return {
                "challenger_attack": self.c_attack,
                "defender_attack": self.d_attack,
                "winner": self.winner,
                "energy": {
                    "challenger": self.challenger.energy,
                    "defender": self.defender.energy
                },
                "hp": {
                    "challenger": self.c_active.hp,
                    "defender": self.d_active.hp
                },
                "decks": {
                    "challenger": self.cdeck,
                    "defender": self.ddeck
                },
                "stat_updates": {
                    "challenger": {
                        "xp": self.c_xp,
                        "hp": self.c_hp,
                        "attack_score": self.c_att_score
                    },
                    "defender": {
                        "xp": self.d_xp,
                        "hp": self.d_hp,
                        "attack_score": self.d_att_score
                    }
                }
            }
