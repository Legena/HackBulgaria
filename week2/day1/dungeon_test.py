import unittest
import dungeon
import sys
import hero
import orc
import weapon
from io import StringIO


class DungeonTests(unittest.TestCase):
    def setUp(self):
        self.dungeon = dungeon.Dungeon("basic_dungeon.txt")

    def test_dungeon_init(self):
        dungeon_file = open("basic_dungeon.txt", 'r')
        self.assertEqual(self.dungeon.map, dungeon_file.read().split('\n'))
        dungeon_file.close()

    def test_dungeon_print_map(self):
        backup = sys.stdout
        self.held, sys.stdout = sys.stdout, StringIO()
        self.dungeon.print_map()
        self.assertEqual(sys.stdout.getvalue().strip('\n'),
        str(self.dungeon.map))
        sys.stdout.close()
        sys.stdout = backup

    def test_dungeon_spawn_hero(self):
        self.hero = hero.Hero("Bron", 100, 'DragonSlayer')
        self.assertTrue(self.dungeon.spawn("player_1", self.hero))
        self.assertTrue(any('H' in line for line in self.dungeon.map))

    def test_dungeon_spawn_orc(self):
        self.orc = orc.Orc("Grom", 100, 2)
        self.assertTrue(self.dungeon.spawn("player_1", self.orc))
        self.assertTrue(any('O' in line for line in self.dungeon.map))

    def test_dungeon_spawn_no_places(self):
        self.hero = hero.Hero("Bron", 100, 'DragonSlayer')
        self.orc = orc.Orc("Grom", 100, 2)
        self.dungeon.spawn("player_1", self.hero)
        self.dungeon.spawn("player_2", self.orc)
        self.assertFalse(self.dungeon.spawn("player_3", self.hero))

    def test_dungeon_move_wall(self):
        self.hero = hero.Hero("Bron", 100, 'DragonSlayer')
        self.dungeon.spawn("player_1", self.hero)
        self.assertFalse(self.dungeon.move("player_1", "left"))

    def test_dungeon_move_obstacle(self):
        self.hero = hero.Hero("Bron", 100, 'DragonSlayer')
        self.dungeon.spawn("player_1", self.hero)
        self.assertFalse(self.dungeon.move("player_1", "down"))

    def test_dungeon_move_path(self):
        self.hero = hero.Hero("Bron", 100, 'DragonSlayer')
        self.dungeon.spawn("player_1", self.hero)
        self.assertTrue(self.dungeon.move("player_1", "right"))

    def test_dungeon_move_fight(self):
        self.hero = hero.Hero("Bron", 200, 'DragonSlayer')
        self.orc = orc.Orc("Grom", 100, 2)
        self.weapon = weapon.Weapon("Axe", 10, 0.5)
        self.hero.equip_weapon(self.weapon)
        self.orc.equip_weapon(self.weapon)
        self.dungeon.spawn("player_1", self.hero)
        self.dungeon.spawn("player_2", self.orc)

        self.assertTrue(self.dungeon.move("player_1", "right"))
        self.assertTrue(self.dungeon.move("player_1", "down"))
        self.assertTrue(self.dungeon.move("player_1", "down"))
        self.assertTrue(self.dungeon.move("player_1", "down"))
        self.assertTrue(self.dungeon.move("player_1", "right"))
        self.assertTrue(self.dungeon.move("player_1", "right"))
        self.assertTrue(self.dungeon.move("player_1", "right"))
        self.assertTrue(self.dungeon.move("player_1", "right"))
        self.assertTrue(self.dungeon.move("player_1", "up"))
        self.assertTrue(self.dungeon.move("player_1", "up"))
        self.assertTrue(self.dungeon.move("player_1", "up"))
        self.assertTrue(self.dungeon.move("player_1", "right"))
        self.assertTrue(self.dungeon.move("player_1", "right"))
        self.assertTrue(self.dungeon.move("player_1", "right"))
        self.assertTrue(self.dungeon.move("player_1", "right"))
        self.assertTrue(self.dungeon.move("player_1", "down"))
        self.assertTrue(self.dungeon.move("player_1", "down"))
        self.assertTrue(self.dungeon.move("player_1", "down"))
        self.assertTrue(self.dungeon.move("player_1", "down"))

if __name__ == '__main__':
    unittest.main()
