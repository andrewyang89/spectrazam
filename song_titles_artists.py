
import numpy as np
from typing import List, Tuple




song_IDs = np.array([])  # Given

song_info = {}  # dictionary mapping song ID to song titles and artists

def identify_song(song_ID: int):
    """
    Identifies and prints the song title and artist given the song ID.
    
    Parameters:
    -----------
    song_ID: int
        The ID of the song to classify.
        
    """
    song, artist = song_info[song_ID]
    print("Song Title: {}".format(song))
    print("Artist: {}".format(artist))
    
    
    
def add_songs(song_name_list: List[str], artist_list: List[str]):
    """
    Adds the list of song names and artists into the database, and 
    updates the list of unique song IDs for each song.
    
    Parameters:
    -----------
    song_name_list: List[str]
        A list containing a string of new song names to add
    artist_list: List[str]
        A corresponding list containing names of the artists
        
    """
    global song_IDs
    new_song_IDs = np.arange(len(song_IDs), len(song_IDs) + len(song_name_list))

    song_IDs = np.arange(len(song_IDs) + len(song_name_list))  #updates song_IDs
    
    for song_ID in new_song_IDs:
        offset = len(song_info)
        song_info[song_ID] = (song_name_list[song_ID-offset], artist_list[song_ID-offset])

def song_name_to_ID(song_name: str) -> int:
    """
    Identifies the unique ID of the song given the name
    
    Parameters:
    -----------
    song_name: str
        Name of song
    
    Returns:
    --------
    song_ID: int
        Unique ID of the song
    """
    song_names = [piece[0] for piece in ID_to_piece.values()]
    song_ID = song_names.index(song_name)
    return song_ID

