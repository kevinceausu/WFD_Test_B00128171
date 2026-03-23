import random

class Artist:
    def __init__(self, name, dob, country, albums=None, songs=None):
        self.name = name
        self.dob = dob
        self.country = country
        self.albums = albums if albums is not None else []
        self.songs = songs if songs is not None else []
    
    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)

    def display_info(self):
        print("Artist Information")
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.dob}")
        print(f"Country: {self.country}")
        print("Albums:", [album.album_title for album in self.albums])
        print("Songs:", [song.song_title for song in self.songs])
        print()



class Song:
    def __init__(self, song_title, artist_name, year_of_release):
        self.song_title = song_title
        self.artist_name = artist_name
        self.year_of_release = year_of_release

    def display_info(self):
        print("Song Information")
        print(f"Song Title: {self.song_title}")
        print(f"Artist Name: {self.artist_name}")
        print(f"Year of Release: {self.year_of_release}")
        print()



class Album:
    def __init__(self, album_title, artist_name, year_of_release, songs=None):
        self.album_title = album_title
        self.artist_name = artist_name
        self.year_of_release = year_of_release
        self.songs = songs if songs is not None else []

    def add_song(self, title, release_year):
        new_song = Song(title, self.artist_name, release_year)
        self.songs.append(new_song)

    def display_info(self):
        print("Album Information")
        print(f"Album Title: {self.album_title}")
        print(f"Artist Name: {self.artist_name}")
        print(f"Year of Release: {self.year_of_release}")
        print("Songs:", [song.song_title for song in self.songs])
        print()



class Playlist:
    def __init__(self, playlist_title, songs=None):
        self.playlist_title = playlist_title
        self.songs = songs if songs is not None else []

    def add_song(self, song):
        self.songs.append(song)

    def print_all_song(self):
        print(f"Playlist: {self.playlist_title}")
        for i, song in enumerate(self.songs, start=1):
            print(f"{i}. {song.song_title} - {song.artist_name} ({song.year_of_release})")
        print()

    def sort_playlist(self, order='ASC'):
        if order == 'ASC':
            self.songs.sort(key=lambda song: song.song_title.lower())
        elif order == 'DES':
            self.songs.sort(key=lambda song: song.song_title.lower(), reverse=True)
        else:
            print("Invalid order. Use 'ASC' or 'DES'.")
        print()

    def shuffle_playlist(self):
        random.shuffle(self.songs)


#demonstrations

#create artist
artist1 = Artist("Taylor Swift", "23/03/2026", "Ireland")

#create album
album1 = Album("Music Album", "Taylor Swift", 2026)

#create 2 songs for the artist
song1 = Song("Our Song", "Taylor Swift", 2026)
song2 = Song("Tim Mcgraw", "Taylor Swift", 2026)

#use add_song() from album class
album1.add_song("Welcome to New York", 1989)
album1.add_song("Blank Space", 1989)

#add the other songs to album
album1.songs.append(song1)
album1.songs.append(song2)

#add_album() and add_song to artist
artist1.add_album(album1)
artist1.add_song(song1)
artist1.add_song(song2)

#add songs created in album1.add_song to artist songs list
for song in album1.songs:
    if song not in artist1.songs:
        artist1.add_song(song)

#create playlist
playlist1 = Playlist("Songs for Web frame development test")

#add songs from album to playlist
for song in album1.songs:
    playlist1.add_song(song)

#display information
artist1.display_info()
album1.display_info()
song1.display_info()

#print all songs from playlist
print("All songs in playlist:")
playlist1.print_all_song()

#sort playlist in ascending order
print("Playlist sorted in ascending order:")
playlist1.sort_playlist('ASC')
playlist1.print_all_song()

#sort in descending order
print("Playlist sorted in descending order:")
playlist1.sort_playlist('DES')
playlist1.print_all_song()

#shuffle aka random playlist
print("Playlist with shuffle:")
playlist1.shuffle_playlist()
playlist1.print_all_song()



