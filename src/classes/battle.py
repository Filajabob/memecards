class Battle:
    def __init__(self, challenger, defender, cdeck, ddeck):

        if not len(cdeck) <= 3 or not len(ddeck) <= 3:
            raise ValueError("Active deck cannot contain more than 3 cards.")

        self.d_active = None
        self.c_active = None

        self.ddeck = cdeck
        self.cdeck = ddeck

        self.challenger = challenger
        self.defender = defender

        self.rotation_num = 1

    def rotate(self, c_active, d_active, attacker, attack):
        self.c_active = self.cdeck[c_active]
        self.d_active = self.ddeck[d_active]

        for i in range(0, 2):
            if attacker == 'c':
                self.attack = getattr(self.c_active, f"{attack}_attack")()

                self.challenger.energy -= self.attack['energy-used']
                self.d_active.hp -= self.attack['damage']
            elif attacker == 'd':
                self.attack = getattr(self.d_active, f"{attack}_attack")()

                self.defender.energy -= self.attack['energy-used']
                self.c_active.hp -= self.attack['damage']
            else:
                raise ValueError(f"Unknown attacker {attacker}, please refer to classes.Battle.rotate.__doc__")

            if self.d_active.hp <= 0:
                self.defender.hp = None
                del self.ddeck[d_active]

            if self.c_active.hp <= 0:
                self.challenger.hp = None
                del self.cdeck[c_active]

            # Too lazy to make it so you can't "go into debt" for energy, maybe will add later
            if (self.challenger.energy <= 0 or len(self.cdeck) == 0) and not (
                    self.defender.energy <= 0 or len(self.ddeck) == 0):
                self.winner = "defender"

            elif not (self.challenger.energy <= 0 or len(self.cdeck) == 0) and (
                    self.defender.energy <= 0 or len(self.ddeck) == 0):
                self.winner = "challenger"

            elif (self.challenger.energy <= 0 or len(self.cdeck) == 0) and (
                    self.defender.energy <= 0 or len(self.cdeck) == 0):
                self.winner = "tie"

            # Make sure the other side gets a turn
            if attacker == 'c':
                attacker = 'd'
            else:
                attacker = 'c'

        self.rotation_num += 1

        return {
            "attack": self.attack,
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
