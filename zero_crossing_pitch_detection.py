from scipy.io import wavfile
from math import ceil
import matplotlib.pyplot as plt

FRAME_SIZE = 4048

def sign(x):
	return -1 if x < 0 else 1

def pitch_detection(filename):
	[sample_rate, signal] = wavfile.read(filename)
	zero_crossings = get_zero_crossings(signal, FRAME_SIZE)
	hzs = get_hz(zero_crossings, FRAME_SIZE, sample_rate)
	fig, axs = plt.subplots(3)
	axs[0].plot(list(map(lambda x: x / sample_rate, range(len(signal)))), signal)
	axs[1].plot(range(len(zero_crossings)), hzs, '-')
	plt.show()


def get_zero_crossings(signal, frame_size):
	zero_crossings = []
	for i in range(len(signal) // frame_size):
		zero_crossing = 0
		for j in range(1, frame_size):
			if sign(signal[j + i * frame_size]) * sign(signal[j - 1 + i * frame_size]) == -1:
				zero_crossing += 1
		zero_crossings.append(zero_crossing)

	return zero_crossings

def get_hz(zero_crossings, frame_size, sample_rate):
	return list(map(lambda x: x / frame_size * sample_rate / 2, zero_crossings))
