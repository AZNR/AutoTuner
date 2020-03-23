import sys
from zero_crossing_pitch_detection import pitch_detection
from autocorrelation_pitch_detection import autocorrelation_pitch_detection

if len(sys.argv) < 2:
	print("specify wav file")
	exit()

pitch_detection(str(sys.argv[1]))
autocorrelation_pitch_detection(str(sys.argv[1]))