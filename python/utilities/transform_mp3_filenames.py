# Extract the artist name from songs with filenames in this format:
#    (number) - (artist) - (title).mp3
# and add the artists name to songs with filenames in this format:
#    (number)..(title).mp3
# to make filenames in this format:
#    (number)..(artist)..(title).mp3
#
#    eg.: 14 - 13th Floor Elevators - You're Gonna Miss Me.mp3
#     +   14..You're Gonna Miss Me.mp3
#     =>  14..13th Floor Elevators..You're Gonna Miss Me.mp3
#
# Copyright 2017 Dave Cuthbert
# MIT License

from __future__ import print_function                   #Not needed with python3

import os as os
import re as re

TARGET_DIR = r"/insert/target/path"

def extract_artist(title):
    artist_regex = re.compile(' - (.*?) - ') 
    artist = artist_regex.search(title)
    return artist.group(1)
    
def get_song_list():
    song_list = os.listdir(os.getcwd())
    return song_list

def get_artists():
    song_list = get_song_list()
    artists = []
    for song in song_list:
        artists.append(extract_artist(song))
    return artists
    
def insert_artist_name():
    artist_names = get_artists()
    old_filenames = os.listdir(TARGET_DIR)
    new_filenames = []
    for (old_filename, artist) in zip(old_filenames, artist_names):
        new_filename = re.sub('\.\.', '..' + artist + '..', old_filename)
        os.rename(os.path.join(TARGET_DIR, old_filename), 
                  os.path.join(TARGET_DIR, new_filename)) 
  
    
    
if "__main__" == __name__:
   #print(*get_artists(), sep='\n')          #DEBUG
   insert_artist_name()