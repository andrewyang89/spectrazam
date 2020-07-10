import pickle
from pathlib import Path

def db_save(song_set: dict, filename="song_database.pkl"):
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

        Notes
        -----
        Will clear any prior data in the file; to append a fingerprint: id,
        key: value pair without clearing the current database, please use
        db_add((<fingerprint>,))

    """
    with open(filename, mode="wb") as database:
        pickle.dump(song_set, database)


def db_load(file_path=Path("./song_database.pkl")):
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
