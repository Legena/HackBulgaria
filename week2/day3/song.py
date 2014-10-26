class Song:
    MAX_RATING = 5
    MIN_RATING = 1

    def __init__(self, title=None, artist=None, album=None,
        rating=None, length=None, bitrate=None):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def rate(self, rate):
        if rate > Song.MAX_RATING or rate < Song.MIN_RATING:
            error_message = "Rating must be from {} to {}"
            raise ValueError(error_message.format(Song.MIN_RATING,
            Song.MAX_RATING))
        else:
            self.rating = rate