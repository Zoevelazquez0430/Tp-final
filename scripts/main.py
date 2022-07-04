import argparse 
from ..Sintetizador.principal_file import sinte
def main() -> None:
    #sinteitzador parser
    parser = argparse.ArgumentParser(description='Sintetizador')
    parser.add_argument('-f', '--input', help='frecuencia')
    parser.add_argument('-i', '--output', help='instrumento')
    parser.add_argument('-p', '--output', help='partitura')
    parser.add_argument('-o', '--tracks', help='audio.wav')

    args = parser.parse_args()
    sinte.generate_track(args.frecuencia, args.instrumento, args.partitura, args.audio.wav)

    #parser2 = argparse.ArgumentParser(description='Metalofono')
    #parser2.add_argument('-p', '--input', help='partitura')
    #parser2.add_argument('-d', '--output', help='dispositivo')

   # args = parser2.parse_args()


if __name__ == '__main__':
    main()
