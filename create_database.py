import song_loading as sl
import find_fingerprints as ff
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion
from scipy.ndimage.morphology import iterate_structure
import querying_tallying_database as qtd

def run():
    ids, music_list = sl.load_music_files("Music/")
    print(ids)
    print(music_list)

    S = {}
    freqs = {}
    times = {}

    for i in range(len(music_list)):
        spectrograms = sl.return_specgram(music_list[i], 44100)
        S[ids[i]] = spectrograms[0]
        freqs[ids[i]] = spectrograms[1]
        times[ids[i]] = spectrograms[2]

    print(S)
    print(freqs)
    print(times)

    fp = iterate_structure(generate_binary_structure(2, 1), 20)

    fingerprints = {}
    for song_id in S:
        fingerprints[song_id] = ff.fingerprint(S[song_id], fp, .1, 5)

    qtd.write_database(fingerprints, "fingerprints_database.pkl")