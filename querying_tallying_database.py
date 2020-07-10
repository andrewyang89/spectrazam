import pickle

import file_management

def write_database(fingerprints, filename):
    """
    Takes fingerprints and writes database and pickle dictionary

    Writes a pickle file with the peaks and the locations that they show up in different songs
    given a dictionary with the song and associated fingerprints,

    Parameters
    ----------
    fingerprints : dictionary
        song : fingerprints [((fm, fn, dt), tm), ...]

    filename : str
        path to write the pickle file
    """
    database = {}
    for song in fingerprints:
        for (fi, fj, dt), tm in fingerprints[song]:
            if not (fi, fj, dt) in database:
                database[(fi, fj, dt)] = []
            database[(fi, fj, dt)].append((song, tm))

    # call writing function with filename parameter
    file_management.db_save(database, filename)


def query_match(clip_fp, filename):
    """
    Find most likely song given a particular clip fingerprint
    Takes fingerprints of the clip and querys them in the database to find most likely song

    Parameters
    ----------
    fingerprints: dictionary
        song : fingerprints [((fm, fn, dt), tm), ...]

    filename : str
        path to read the pickle file
    """
    with open(filename, mode="rb") as opened_file:
        database = pickle.load(opened_file)

    tally = {}
    for (fm, fn, dt), t_clip in clip_fp:
        if not (fm, fn, dt) in database:
            continue
        for song, t_song in database[(fm, fn, dt)]:
            t_offset = t_song - t_clip
            if not (song, t_offset) in tally:
                tally[(song, t_offset)] = 0
            tally[(song, t_offset)] += 1

    if tally:
        likely_song, offset = max(tally, key=tally.get)
        print(f"Tally{tally[(likely_song, offset)]}")
        return tally, likely_song
    return {}, -1  # Indicating no peaks matching
