import argparse 
from principal_file import Sintetizer

#sythesizer parser
parser = argparse.ArgumentParser(description='Sintetizador')
parser.add_argument('-f', '--frequency', help='frequency')
parser.add_argument('-i', '--instrument', help='instrument')
parser.add_argument('-p', '--score', help='score')
parser.add_argument('-o', '--output', help='audio.wav')

args = parser.parse_args()
frequency= args.frequency
instrument= args.instrument
score= args.score
audio= args.output

sinte= Sintetizer(frequency, instrument, score, audio)

if __name__ == '__main__':
    sinte.generate_track(audio, frequency)