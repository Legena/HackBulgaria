import weapon

class Entity:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.__weapon = None
        self.__max_health = self.health

    def get_health(self):
        return self.health

    def is_alive(self):
        if(self.health > 0):
            return True
        else:
            return False

    def take_damage(self, damage_points):
        if(damage_points > self.health):
            self.health = 0
        else:
            self.health -= damage_points

    def take_healing(self, healing_points):
        if(self.health > 0):
            if((self.health + healing_points) > self.__max_health):
                self.health = self.__max_health
            else:
                self.health += healing_points
        else:
            return False
        return True

    def has_weapon(self):
        if isinstance(self.__weapon, weapon.Weapon):
            return True
        else:
            return False

    def equip_weapon(self, weapon):
        self.__weapon = weapon

    def attack(self):
        if self.has_weapon():
            if self.__weapon.critical_hit():
                return self.__weapon.damage * 2
            else:
                return self.__weapon.damage
        else:
            return 0