import entity
import weapon
import unittest


class EntityTests(unittest.TestCase):
    def setUp(self):
        self.test_entity = entity.Entity("Test", 100)

    def test_entity_get_health(self):
        self.assertEqual(self.test_entity.get_health(), 100)

    def test_entity_is_alive(self):
        self.assertTrue(self.test_entity.is_alive())
        self.test_entity.health = 0
        self.assertFalse(self.test_entity.is_alive())

    def test_entity_take_damage_integer(self):
        self.test_entity.take_damage(8)
        self.assertEqual(self.test_entity.get_health(), 92)

    def test_entity_take_damage_float(self):
        self.test_entity.take_damage(3.14)
        self.assertEqual(self.test_entity.get_health(), 96.86)

    def test_entity_take_damage_more_than_health(self):
        self.test_entity.take_damage(150)
        self.assertEqual(self.test_entity.get_health(), 0)

    def test_entity_take_healing_max_health(self):
        self.assertTrue(self.test_entity.take_healing(5))

    def test_entity_take_healing_damaged(self):
        self.test_entity.health = 50
        self.assertTrue(self.test_entity.take_healing(9))

    def test_entity_take_healing_death(self):
        self.test_entity.health = 0
        self.assertFalse(self.test_entity.take_healing(10))

    def test_entity_has_weapon_none(self):
        self.assertFalse(self.test_entity.has_weapon())

    def test_entity_equip_weapon(self):
        self.assertFalse(self.test_entity.has_weapon())
        self.test_entity.equip_weapon(weapon.Weapon("axe", 10, 0.5))
        self.assertTrue(self.test_entity.has_weapon())

    def test_entity_attack_no_weapon(self):
        self.assertEqual(self.test_entity.attack(), 0)

    def test_entity_attack_no_crit(self):
        self.test_entity.equip_weapon(weapon.Weapon("bow", 10, 0))
        self.assertEqual(self.test_entity.attack(), 10)

    def test_entity_attack_crit(self):
        self.test_entity.equip_weapon(weapon.Weapon("sword", 15, 1))
        self.assertEqual(self.test_entity.attack(), 30)

if __name__ == '__main__':
    unittest.main()