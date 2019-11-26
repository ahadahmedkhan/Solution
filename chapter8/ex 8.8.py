def make_album(artist,title,tracks=0):
    album_info={'Artist_name':artist.title(),
                'Title':title.title(),
                }
    if tracks:
            album_info['Tracks']= tracks
    return album_info
while True:
    title_name=input('Please enter the name of title of album.  ')
    if title_name == 'quit':
        break
    artist_name=input('\nPlease enter the name of artist of album.  ')
    if artist_name=='quit':
        break
    no_of_tracks=str(input('\nPlease enter no of tracks if any . '))
    print("\nenter 'quit to stop at any time !!")
    if no_of_tracks=='quit':
        break
    print(make_album(artist_name,title_name,int(no_of_tracks)))
print("thanks for responding !!")