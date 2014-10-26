from entity import Entity
from random import randint


class Fight():
    def __init__(self, fighter, enemy):
        self.fighter = fighter
        self.enemy = enemy

    def simulate_fight(self):
        if self.fighter.has_weapon() or self.enemy.has_weapon():
            side = randint(0, 100)
            if side < 50:
                self.enemy.take_damage(self.fighter.attack())
                print("%s hits %s for %f." % (self.fighter.name,
                self.enemy.name, self.fighter.attack()))
            while(self.fighter.health > 0 and self.enemy.health > 0):
                self.fighter.take_damage(self.enemy.attack())
                print("%s hits %s for %f." % (self.enemy.name,
                self.fighter.name, self.enemy.attack()))
                if self.fighter.health == 0:
                    return 2
                self.enemy.take_damage(self.fighter.attack())
                print("%s hits %s for %f." % (self.fighter.name,
                self.enemy.name, self.fighter.attack()))
                if self.enemy.health == 0:
                    return 1
        else:
            return 0