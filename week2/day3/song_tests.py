import unittest

from song import Song


class SongTests(unittest.TestCase):
    def setUp(self):
        self.test_song = Song(
            "Hells Bells",
            "ACDC",
            "Back in Black",
            5,
            312,
            320
            )

    def test_song_init(self):
        self.assertEqual(self.test_song.title, "Hells Bells")
        self.assertEqual(self.test_song.artist, "ACDC")
        self.assertEqual(self.test_song.album, "Back in Black")
        self.assertEqual(self.test_song.rating, 5)
        self.assertEqual(self.test_song.length, 312)
        self.assertEqual(self.test_song.bitrate, 320)

    def test_song_rate(self):
        self.test_song.rate(3)
        self.assertEqual(self.test_song.rating, 3)

    def test_song_rate_out_of_range(self):
        with self.assertRaises(ValueError):
            self.test_song.rate(8)

if __name__ == '__main__':
    unittest.main()