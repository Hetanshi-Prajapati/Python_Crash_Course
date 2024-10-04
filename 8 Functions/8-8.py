"""def make_album(ar_name,al_title):
    music_album={
        'a_name':ar_name,
        'a_title':al_title
    }
    
    return music_album

# info1=make_album('abc','pqr')
# print(info1)
# info2=make_album('ghi','jkl')  
# print(info2)  

while True:
    ar_name=input("Enter album's artist: ")
    if ar_name=='quit':
        break
    
    al_title=input("Enter album's title: ")
    if al_title=='quit':
        break
    
    print(f"album: {music_album}")"""
    
def make_album(artist_name, album_title, number_of_songs=None):
    """Builds a dictionary describing a music album."""
    album = {
        'artist': artist_name,
        'title': album_title
    }
    
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    
    return album

# Continuously prompt user for album information
while True:
    print("\nEnter the artist and album title (or type 'quit' to exit).")
    
    artist = input("Artist name: ")
    if artist.lower() == 'quit':
        break
    
    title = input("Album title: ")
    if title.lower() == 'quit':
        break
    
    songs = input("Number of songs (optional, press Enter to skip): ")
    if songs.lower() == 'quit':
        break
    
    # Check if songs input is provided, and handle conversion properly
    if songs:
        try:
            album = make_album(artist, title, int(songs))
        except ValueError:
            print("Please enter a valid number for the songs.")
            continue  # Go back to the start of the loop if input is invalid
    else:
        album = make_album(artist, title)
    
    print(f"Created album: {album}")
