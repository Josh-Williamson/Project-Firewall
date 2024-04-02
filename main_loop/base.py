class Base:
    def __init__(self):
        self.hp = 10

    def get_hp(self):
        return self.hp

    def baseDamage(self, enemy):
        self.hp = self.hp - enemy.damage
        return
