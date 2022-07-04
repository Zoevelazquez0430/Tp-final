import argparse 
from Sintetizador.principal_file import sinte
def main() -> None:
    #sinteitzador parser
    parser = argparse.ArgumentParser(description='Sintetizador')
    parser.add_argument('-f', '--input', help='frecuencia')
    parser.add_argument('-i', '--output', help='instrumento')
    parser.add_argument('partitura', '--output', help='partitura')
    parser.add_argument('-o', '--tracks', help='audio.wav')

    args = parser.parse_args()
    sinte.generate_track(args.partitura, args.instrumento)


if __name__ == '__main__':
    main()
