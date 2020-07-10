import pickle
from pathlib import Path

def save(song_set: dict, filename="song_database.pkl"):
    """Saves the input database in binary

        Parameters
        ----------
        song_set : dict
            The database of songs to be used as the test set

        file_name : str
            The file name (.pkl) to save the database as (defaults to
            "song_database.pkl")

        Returns
        -------
        None

    """
    # pickling the song dictionary
    with open(filename, mode="wb") as database:
        pickle.dump(song_set, database)


def load(file_path=Path("./song_database.pkl")):
    """Loads a read-only version of the database in binary

        Parameters
        ----------
        file_path : pathlib.Path
            The file path to the database (loads "./song_database.pkl" by
            default)

        Returns
        -------
        None

        Notes
        -----
        You can only access the file from its first superdirectory; any attempt
        to access the database file from a
        super-er superdirectory will raise a FileNotFoundError

    """

    with open(file_path, mode="rb") as database:
        return pickle.load(database)


def
