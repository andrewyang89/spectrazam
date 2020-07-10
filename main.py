import ID_to_piece
import song_loading as sl
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion, iterate_structure
import numpy as np
import find_fingerprints as ff
import querying_tallying_database as qtd


def run(duration):
    samples, sampling_rate = sl.record_sound(duration)

    print(f"Sampling rate: {sampling_rate}")
    spec = sl.return_specgram(samples, sampling_rate)[0]

    fp = iterate_structure(generate_binary_structure(2, 1), 20)

    fingerprints = ff.fingerprint(spec, fp, np.percentile(spec, 75), 15)

    tally, song = qtd.query_match(fingerprints, "fingerprints_database.pkl")

    print(ID_to_piece.ID_to_piece[song])
    print(tally)
