from song import Song
from playlist import Playlist
from mutagen.mp3 import MP3
import os
import glob


class MusicCrawler:
    def __init__(self, filepath):
        self.songs = []

    def generate_playlist(self, filepath):
        os.chdir(filepath)
        songs = glob.glob('*.mp3')
        playlist = Playlist("new")
        for song in songs:
            audio = MP3(song)
            song_to_add = Song(audio["TIT2"].text, audio["TPE1"].text,
            audio["TALB"].text, 0, round(audio.info.length),
            audio.info.bitrate // 1000)
            playlist.add_song(song_to_add)
        self.songs = playlist