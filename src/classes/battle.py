from .errors import BattleEnded


class Battle:
    def __init__(self, challenger, defender, cdeck, ddeck, save_results=True):

        if not len(cdeck) <= 3 or not len(ddeck) <= 3:
            raise ValueError("Active deck cannot contain more than 3 cards.")

        self.d_active = None
        self.c_active = None

        self.ddeck = ddeck
        self.cdeck = cdeck

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

        :param d_attack:
        :param c_attack:
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
                elif c_attack == "secondary":
                    self.attack = self.c_active.secondary_attack()
                elif c_attack == "special":
                    self.attack = self.c_active.special_attack()

                self.c_attack = self.attack
                self.challenger.energy -= self.attack['energy-used']
                self.d_active.hp -= round(self.attack['damage'], 2)

            elif attacker == 'd':
                if d_attack == "primary":
                    self.attack = self.d_active.primary_attack()
                elif d_attack == "secondary":
                    self.attack = self.d_active.secondary_attack()
                elif d_attack == "special":
                    self.attack = self.d_active.special_attack()

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
            if (self.challenger.energy <= 0 or len(self.cdeck) == 0) and not (
                    self.defender.energy <= 0 or len(self.ddeck) == 0):
                self.winner = "defender"
                break

            elif not (self.challenger.energy <= 0 or len(self.cdeck) == 0) and (
                    self.defender.energy <= 0 or len(self.ddeck) == 0):
                self.winner = "challenger"
                break

            elif (self.challenger.energy <= 0 or len(self.cdeck) == 0) and (
                    self.defender.energy <= 0 or len(self.cdeck) == 0):
                self.winner = "tie"
                break

            # Make sure the other side gets a turn
            if attacker == 'c':
                attacker = 'd'
            else:
                attacker = 'c'

        self.rotation_num += 1

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
