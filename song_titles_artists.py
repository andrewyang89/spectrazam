import numpy as np
from typing import List, Tuple
import song_loading as sl
from ID_to_piece import ID_to_piece

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

    song_IDs = np.arange(len(song_IDs) + len(song_name_list))  # updates song_IDs

    for song_ID in new_song_IDs:
        offset = len(song_info)
        song_info[song_ID] = (song_name_list[song_ID - offset], artist_list[song_ID - offset])


def song_artist_to_songs(artist_name: str) -> List[str]:
    """
    Identifies the names of songs in the database by given artist.
    
    Parameters:
    -----------
    artist_name: str
        Name of artist
    
    Returns:
    --------
    songs: List[str]
        List of songs by given artist
    """
    
    song_names = [piece[0] for piece in ID_to_piece.values()]  #list of all songs
    artist_names = [piece[1] for piece in ID_to_piece.values()]  #list of all artists
    song_IDs = [index for index, element in enumerate(artist_names) if element == artist_name]  #ID's of songs with input artist
    songs = [song_names[i] for i in song_IDs]
    return songs

def check_song(song_name: str) -> bool:
    """
    Checks if a song is in the dictionary.
    
    Parameters:
    -----------
    song_name: str
        Name of input song
    
    Returns:
    --------
    exists: bool
        Does the song exist in the database?
    """
    song_names = [piece[0] for piece in ID_to_piece.values()]  #list of all songs
    return song_name in song_names

def delete_song_name(song_name: str):
    """
    Deletes song name from ID_to_piece dictionary
    
    Parameters:
    -----------
    song_name: str
        Name of song to be deleted
    """
    
    ID_to_piece.pop(song_name_to_ID(song_name))
    
    
def song_name_to_ID(names: list) -> dict:
    """
        Provides the unique ID of the song given the name

        Parameters:
        -----------
        names: List
            List of names

        Returns:
        --------
        dictionary: dict
            Dictionary of unique IDs and songs
        """
    dictionary = {names[i]: i for i in range(len(names))}
    return dictionary
