import json
from song import Song


class Playlist:
    LOW_BITRATE = 128

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, title):
        self.songs = [song for song in self.songs if song.title != title]

    def total_length(self):
        length = 0
        for song in self.songs:
            length += song.length
        return length

    def remove_disrated(self, rating):
        self.songs = [song for song in self.songs if song.rating >= rating]

    def remove_bad_quality(self):
        self.songs = [song for song in self.songs if
        song.bitrate >= Playlist.LOW_BITRATE]

    def show_artists(self):
        artists = set()
        for song in self.songs:
            artists.add(song.artist)
        return artists

    def __length_to_str__(self, length):
        return "{:02d}:{}".format(length // 60, length % 60)

    def __str__(self):
        result = ""
        for song in self.songs:
            result += "{} {} - {}\n".format(song.artist, song.title,
            self.__length_to_str__(song.length))
        result = result[:-1]
        return result

    def save(self, file_name):
        result = {}
        result["name"] = self.name
        result["songs"] = []
        for song in self.songs:
            result["songs"].append(song.__dict__)
        save_file = open(file_name, "w")
        save_file.write(json.dumps(result))
        save_file.close()

    def load(self, file_name):
        read_file = open(file_name, "r")
        result = json.load(read_file)
        count = 0
        for song in result["songs"]:
            self.songs.append(Song())
            self.songs[count].__dict__.update(song)
            count += 1
        print(self.__str__())