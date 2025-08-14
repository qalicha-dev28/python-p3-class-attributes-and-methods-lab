class Song:
    #attributes
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}


    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_artist(artist)
        self.add_genre(genre)

        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_artist(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
    
 # example usage
starships = Song("Starships", "Nicki Minaj", "Pop")
gold_digger = Song("Gold Digger", "Kanye West", "Hip-Hop")
rhumba_japani = Song("Rhumba Japani", "Miriam Makeba", "World")
medicine = Song("Medicine", "Bensoul", "Afro-Fusion")
    
print(Song.count)
print(Song.artists)
print(Song.genres)
print(Song.genre_count)
print(Song.artist_count)



