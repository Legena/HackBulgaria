import unittest

from playlist import Playlist
from song import Song


class PlaylistTests(unittest.TestCase):
    def setUp(self):
        self.test_playlist = Playlist("Test")
        self.test_song = Song(
            "Hells Bells",
            "ACDC",
            "Back in Black",
            5,
            312,
            320
            )

    def test_playlist_init(self):
        self.assertEqual(self.test_playlist.name, "Test")

    def test_playlist_add_song(self):
        self.test_playlist.add_song(self.test_song)
        self.assertIn(self.test_song, self.test_playlist.songs)

    def test_playlist_remove_song(self):
        self.test_playlist.add_song(self.test_song)
        self.test_song_second = Song(
            "Back in Black",
            "ACDC",
            "Back in Black",
            5,
            312,
            320
            )
        self.test_playlist.add_song(self.test_song_second)
        self.test_playlist.remove_song(self.test_song.title)
        self.assertNotIn(self.test_song, self.test_playlist.songs)
        self.assertIn(self.test_song_second, self.test_playlist.songs)

    def test_playlist_remove_multiple(self):
        for count in range(0, 3):
            self.test_playlist.add_song(self.test_song)
        self.test_playlist.remove_song(self.test_song.title)
        self.assertNotIn(self.test_song, self.test_playlist.songs)

    def test_playlist_total_length(self):
        for count in range(0, 3):
            self.test_playlist.add_song(self.test_song)
        self.assertEqual(self.test_playlist.total_length(), 936)

    def test_playlist_remove_disrated(self):
        self.test_playlist.add_song(self.test_song)
        self.test_song_second = Song(
            "Back in Black",
            "ACDC",
            "Back in Black",
            2,
            312,
            320
            )
        self.test_playlist.add_song(self.test_song_second)
        self.test_playlist.remove_disrated(3)
        self.assertEqual(len(self.test_playlist.songs), 1)

    def test_playlist_remove_bad_quality(self):
        self.test_playlist.add_song(self.test_song)
        self.test_song_second = Song(
            "Back in Black",
            "ACDC",
            "Back in Black",
            5,
            312,
            64
            )
        self.test_playlist.add_song(self.test_song_second)
        self.test_playlist.remove_bad_quality()
        self.assertEqual(len(self.test_playlist.songs), 1)

    def test_playlist_show_artists(self):
        self.test_playlist.add_song(self.test_song)
        self.test_song_second = Song(
            "Back in Black",
            "ACDC",
            "Back in Black",
            5,
            312,
            320
            )
        self.test_playlist.add_song(self.test_song_second)
        self.assertEqual(self.test_playlist.show_artists(), {'ACDC'})

    def test_playlist_str(self):
        self.test_playlist.add_song(self.test_song)
        self.test_song_second = Song(
            "Back in Black",
            "ACDC",
            "Back in Black",
            5,
            250,
            320
            )
        self.test_playlist.add_song(self.test_song_second)
        self.assertEqual(str(self.test_playlist),
        "ACDC Hells Bells - 05:12\nACDC Back in Black - 04:10")

    def test_playlist_save(self):
        self.test_playlist.add_song(self.test_song)
        self.test_song_second = Song(
            "Back in Black",
            "ACDC",
            "Back in Black",
            5,
            250,
            320
            )
        self.test_playlist.add_song(self.test_song_second)
        self.test_playlist.save("gg")

    def test_playlist_load(self):
        self.test_playlist.load("gg")

if __name__ == '__main__':
    unittest.main()