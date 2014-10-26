import unittest
import orc
import hero
import weapon
import fight


class FightTests(unittest.TestCase):
    def setUp(self):
        self.hero_test = hero.Hero("Teddy", 500, "Bear")
        self.orc_test = orc.Orc("Grom", 100, 2)
        self.weapon_test = weapon.Weapon("Gorehowl", 25, 0.5)
        self.fight = fight.Fight(self.hero_test, self.orc_test)

    def test_fight_no_damage(self):
        self.assertEqual(self.fight.simulate_fight(), 0)

    def test_fight_one_side_damage(self):
        self.hero_test.equip_weapon(self.weapon_test)
        self.assertEqual(self.fight.simulate_fight(), 1)

    def test_fight_both_side_damage(self):
        self.hero_test.equip_weapon(self.weapon_test)
        self.orc_test.equip_weapon(self.weapon_test)
        self.assertEqual(self.fight.simulate_fight(), 1)

if __name__ == '__main__':
    unittest.main()