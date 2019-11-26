def make_album(artist,title,tracks=0):
    album_info={'Artist_name':artist.title(),
                'Title':title.title(),
                }
    if tracks:
            album_info['Tracks']= tracks
    return album_info
print(make_album('ali zafar','albela',8))
print(make_album('atif aslam','jannat'))
print(make_album('nfak','dua',4))