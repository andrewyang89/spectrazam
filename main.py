import song_loading as sl
import song_titles_artists as sta

sampling_rate = 44100
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

# samples, rate = sl.record_sound(2)
# print(samples)
# print(rate)
# print(samples.shape)
# spec = sl.return_specgram(samples, rate)[0]
# print(spec)

