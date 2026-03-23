import unittest
from PartA import Artist, Song, Album, Playlist

class TestIfObjectInstance(unittest.TestCase):
    def test_artist_instance(self):
        artist = Artist("Taylor Swift", "23/03/2026", "Ireland")
        self.assertIsInstance(artist, Artist)

    def test_song_instance(self):
        song = Song("Tim Mcgraw", "Taylor Swift", 2026)
        self.assertIsInstance(song, Song)

    def test_album_instance(self):
        album = Album("Music Album", "Taylor Swift", 2026)
        self.assertIsInstance(album, Album)

    def test_playlist_instance(self):
        playlist = Playlist("Songs for Web frame development test")
        self.assertIsInstance(playlist, Playlist)


class TestNotInstance(unittest.TestCase):
    def test_artist_not_instance(self):
        artist = Artist("Taylor Swift", "01/01/2000", "USA")
        self.assertNotIsInstance(artist, Song)

    def test_song_not_instance(self):
        song = Song("Style", "Taylor Swift", 2014)
        self.assertNotIsInstance(song, Album)

    def test_album_not_instance(self):
        album = Album("1989", "Taylor Swift", 2014)
        self.assertNotIsInstance(album, Playlist)

    def test_playlist_not_instance(self):
        playlist = Playlist("My Playlist")
        self.assertNotIsInstance(playlist, Artist)


class TestIdenticalSimilar(unittest.TestCase):
     def test_identical_objects(self):
        song1 = Song("Blank Space", "Taylor Swift", 1989)
        song2 = song1  #same object

        self.assertIs(song1, song2)

     def test_similar_but_not_identical_objects(self):
        song1 = Song("Blank Space", "Taylor Swift", 2014)
        song2 = Song("Blank Space", "Taylor Swift", 2014)  #similar object

        self.assertIsNot(song1, song2)   


class TestMethods(unittest.TestCase):
    def test_artist_add_song(self):
        artist = Artist("Taylor Swift", "23/03/2026", "Ireland")
        song = Song("Blank Space", "Taylor Swift", 1989)
        artist.add_song(song)

        self.assertIn(song, artist.songs)

    def test_artist_add_album(self):
        artist = Artist("Taylor Swift", "23/03/2026", "Ireland")
        album = Album("Music Album", "Taylor Swift", 2026)

        artist.add_album(album)

        self.assertIn(album, artist.albums)

    def test_album_add_song(self):
        album = Album("Music Album", "Taylor Swift", 2026)

        album.add_song("Welcome to New York", 1989)
#check if a song in that album exists with that name
        self.assertTrue(any(song.song_title == "Welcome to New York" for song in album.songs))

    def test_playlist_add_song(self):
        playlist = Playlist("Songs for Web Frame development test")
        song = Song("Blank Space", "Taylor Swift", 1989)

        playlist.add_song(song)

        self.assertIn(song, playlist.songs)

if __name__ == "__main__":
    unittest.main()