import weapon
import orc
import unittest


class OrcTests(unittest.TestCase):
    def setUp(self):
        self.jamal_orc = orc.Orc("Jamal", 100, 2)

    def test_orc_init(self):
        self.assertEqual(self.jamal_orc.name, 'Jamal')
        self.assertEqual(self.jamal_orc.health, 100)
        self.assertEqual(self.jamal_orc.berserk_factor, 2)
        self.jamal_orc = orc.Orc("Jamal", 100, 4)
        self.assertEqual(self.jamal_orc.berserk_factor, 2)
        self.jamal_orc = orc.Orc("Jamal", 100, 0)
        self.assertEqual(self.jamal_orc.berserk_factor, 1)
        self.jamal_orc = orc.Orc("Jamal", 100, 1)
        self.assertEqual(self.jamal_orc.berserk_factor, 1)

    def test_orc_attack(self):
        self.jamal_orc.equip_weapon(weapon.Weapon("mace", 20, 1))
        self.assertEqual(self.jamal_orc.attack(), 80)

if __name__ == '__main__':
    unittest.main()