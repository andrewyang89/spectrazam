import pickle
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
    db_save(database, filename)

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
    # call reading function with filename parameter
    database = db_load(filename)

    tally = {}
    for (fm, fn, dt), t_clip in clip_fp:
        if not fp in database:
            continue
        song, t_song = database[(fm, fn, dt)]
        t_offset = t_song - t_clip
        if not (song, t_offset) in tally:
            tally[(song, t_offset)] = 0
        tally[(song, t_offset)] += 1

    likely_song, offset = max(tally, key=tally.get)
    return tally, likely_song
