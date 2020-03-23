from scipy.io import wavfile
from math import ceil
import matplotlib.pyplot as plt

FRAME_SIZE = 4048
SKIP_SIZE = 10

def normalize_signal(signal):
	max_val = max(signal, key=abs)
	return list(map(lambda x: x / abs(max_val), signal))

def autocorrelate(signal, frame_start, frame_size, lag):
	summation = 0
	for i in range(frame_size - lag):
		summation += signal[frame_start + i] * signal[frame_start + i + lag] / frame_size
	return summation

def autocorrelation_of_frame(signal, frame_start, frame_size):
	autocorrelation_values = []
	for i in range(frame_size // SKIP_SIZE):
		autocorrelation_values.append(autocorrelate(signal, frame_start, frame_size, i * 10))
	return autocorrelation_values

def calculate_frequency(autocorrelation_max, sample_rate):
	return sample_rate / autocorrelation_max

def autocorrelation_pitch_detection(filename):
	[sample_rate, signal] = wavfile.read(filename)
	norm_signal = normalize_signal(signal)
	#norm_signal = signal
	max_signal = max(signal, key=abs)
	frequencies = []
	for i in range(len(signal) // FRAME_SIZE):
		print(i)
		autocorrelation_values = autocorrelation_of_frame(norm_signal, FRAME_SIZE * i, FRAME_SIZE)
		j = 0
		prev = 1
		while (autocorrelation_values[j] < prev):
			prev = autocorrelation_values[j]
			j+=1
		while (autocorrelation_values[j] > prev):
			prev = autocorrelation_values[j]
			j+=1
		j-=1
		frequencies.append(sample_rate / j / SKIP_SIZE)
		print(max(autocorrelation_values[j:]))
	fig, axs = plt.subplots(3)
	fig.suptitle('Vertically stacked subplots')
	axs[0].plot(list(map(lambda x: x / sample_rate, range(len(signal)))), norm_signal)
	axs[1].plot(range(len(frequencies)), frequencies, '-')
	plt.show()
	return frequencies



