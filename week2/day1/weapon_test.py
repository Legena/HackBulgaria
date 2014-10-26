import weapon
import unittest


class WeaponTests(unittest.TestCase):
    def setUp(self):
        self.axe_weapon = weapon.Weapon("axe", 10, 1)

    def test_weapon_init(self):
        self.assertEqual(self.axe_weapon.type, "axe")
        self.assertEqual(self.axe_weapon.damage, 10)
        self.assertEqual(self.axe_weapon.critical_strike_percent, 1)

    def test_critical_strike(self):
        self.assertTrue(self.axe_weapon.critical_hit())

    def test_critical_strike_none(self):
        self.axe_weapon.critical_strike_percent = 0
        self.assertFalse(self.axe_weapon.critical_hit())


if __name__ == '__main__':
    unittest.main()