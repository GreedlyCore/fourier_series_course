data, sample_rate = librosa.load('accord7.mp3')
sound_from_time = np.vectorize(lambda t: data[int(t * sample_rate)])
# remove some time to aboid problem with indexing
length = len(data) / sample_rate - 0.005
print(length)
