import pickle
from pathlib import Path

def db_save(song_set: dict, filename="song_database.pkl"):
    """Saves the input database in binary

        Parameters
        ----------
        song_set: dict
            The database of songs to be used as the test set

        file_name: str
            The file name (.pkl) to save the database as (defaults to
            "song_database.pkl")

        Returns
        -------
        None

        Notes
        -----
        Will clear any prior data in the file; please review your input before
        running this command.

    """
    with open(filename, mode="wb") as database:
        pickle.dump(song_set, database)


def db_load(file_path=Path("./song_database.pkl")):
    """Loads a read-only version of the database in binary

        Parameters
        ----------
        file_path: pathlib.Path
            The file path to the database (loads "./song_database.pkl" by
            default)

        Returns
        -------
        database: pointer?
            (Should be) A reference to the database .pkl file

        Notes
        -----
        You can only access the file from its first superdirectory; any attempt
        to access the database file from a super-er superdirectory will raise a
        FileNotFoundError

    """
    with open(file_path, mode="rb") as database:
        return pickle.load(database)


def delete_song(database, song_name: str):
    """Removes the specified song from the database and returns the data upon
        completion

        Parameters
        ----------
        database: dict
            The database of fingerprint: song ID pairs

        song_name: str
            The title of the song to be removed

        Returns
        -------
        Tuple[bool, Tuple]
        delere: bool
            Whether or not a fingerprint: song pair with the specified song name
            was removed from the database
        deleted: Tuple[str, str]
            A tuple containing the piece name and the contributors, respectively

        Notes
        -----
        Only functions properly given that no duplicate song values can be/have
        been added

        WILL NOT REMOVE SONG IDS FROM ANY CONVERSION DICTIONARY; INFORMATION CAN
        ONLY BE WITHDRAWN FROM THE FINGERPRINT DATABASE

        I wrote that in all caps because I want to minimize conflicts around
        adding and ID reassignment (as in "Don't do it, please just create a new
        one")

    """
    delere = False
    deleted = None
    song_id = song_name_to_ID(song_name)
    for fingerprint in database:
        if database[fingerprint] == song_id:
            deleted = database.pop(fingerprint)
            delere = True
    return (delere, deleted)
