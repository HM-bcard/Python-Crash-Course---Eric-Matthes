def make_album(artist=None,album=None,no_of_songs = None):
    album_data = {}
    artist = input("Input the name of the artist   ")
    album = input("Input the name of the album   ")
    album_data[artist] = album
    return album_data

while True:
    print("\nPlease tell me the name of the artist: ")
    print("(enter 'q' any time to quit)")
    artist = input("artist's name: ")
    if artist == 'q':
        break
    album = input("album name: ")
    if album == 'q':
        break
    
    new_album = make_album(artist,album)
    print(f"The album is {new_album[artist]} by {artist} ")

    
