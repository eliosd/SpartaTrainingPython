class Pokemon:
    def __init__(self, name, type, hp, attack, defence):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.lvl = 1
        self.moves = []

    def receive_attack(self, power, is_super_affective=False):
        if is_super_affective:
            self.hp -= (power - self.defence) * 1.5
        else:
            self.hp -= (power - self.defence)

    def lvl_up(self, levels=1):
        self.lvl += levels
        self.hp += levels * 2
        self.attack += levels
        self.defence += levels