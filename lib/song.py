class Song:
    # Class attributes that track information about all songs
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Store information about this specific song
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update the library statistics whenever a song is created
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        # Increase the total number of songs by one
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Add the genre only if it is not already in the list
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Add the artist only if they are not already in the list
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Increase the genre count or create it if it does not exist
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        # Increase the artist count or create it if it does not exist
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1