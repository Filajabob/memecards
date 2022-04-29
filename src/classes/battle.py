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

    def rotate(self, c_active, d_active, attacker):
        self.c_active = self.cdeck[c_active]
        self.d_active = self.ddeck[d_active]



