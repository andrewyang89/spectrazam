#!/usr/bin/env python
# coding: utf-8


import numpy as np
import librosa
from pathlib import Path

from microphone import record_audio

import matplotlib.mlab as mlab

from os import listdir
from os.path import isfile, join


def load_song_from_path(path: str):
    """
    Loads a song from a path.

    Returns the samples, sampling rate, and duration.

    Parameters
    ------------
    path: str
          The path for the specified audio file

    Returns
    -------
    Tuple[np.narray, int, float]
        The list of samples, the sampling rate and the duration of the song
    """
    song_path = Path(path)
    samples, sampling_rate = librosa.load(song_path, sr=None)
    duration = librosa.get_duration(y=samples, sr=sampling_rate)

    return samples, sampling_rate, duration


def load_music_files(directory: str):
    """
    Loads the files in a folder.

    Returns the samples from each file.

    Parameters
    ------------
    directory: str
          The path for the specified folder

    Returns
    -------
    List
        Names of all of the songs
    np.ndarray size: (M,N)
        The array of samples for each song
    """
    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    music_list = np.array([load_song_from_path(directory + paths)[0] for paths in files])
    return files, music_list


def return_specgram(samples: np.ndarray, sampling_rate: int):
    """
    Creates the spectrogram for a specific set of samples

    Returns the spectrogram, the frequencies, and the times

    Parameters
    ------------
    samples: np.ndarray
          The array of samples
    sampling_rate: int
          The sampling rate
    Returns
    -------
    Tuple[np.narray, np.narray, np.narray]
        The spectrogram 2d array, the frequencies and the timestamps
    """
    S, freqs, times = mlab.specgram(
        samples,
        NFFT=4096,
        Fs=sampling_rate,
        window=mlab.window_hanning,
        noverlap=int(4096 / 2),
        mode='magnitude'
    )
    return S, freqs, times


def record_sound(time: float):
    """
    Records sound for a specific duration of time

    Returns the frames and the sample rate

    Parameters
    ------------
    time: float
          The duration of the recording in seconds

    Returns
    -------
    Tuple[np.narray, int]
        The frames and the sample rate
    """
    listen_time = time  # seconds
    frames, sample_rate = record_audio(listen_time)
    samples = np.empty(0)
    for i in frames:
        samples = np.append(samples, np.frombuffer(i, np.int16))
    return samples, sample_rate
