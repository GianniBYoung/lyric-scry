#!/usr/bin/python3
# Author: Gianni Young 06/03/2021
import sys
import lyricsgenius
genius = lyricsgenius.Genius("that's one dead space marine.")

givenSong = str(sys.argv[1])

if len(sys.argv) == 3:
    givenArtist = str(sys.argv[2])
    song = genius.search_song(givenSong, givenArtist, get_full_info=False)

else:
    song = genius.search_song(givenSong, get_full_info=False)
    
print(song.lyrics)


    
