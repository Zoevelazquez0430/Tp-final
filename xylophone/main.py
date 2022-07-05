from fileinput import filename
from xylophone.client import XyloClient
from xylo_reader import xilo_sheet_reader
import argparse

parser = argparse.ArgumentParser(description='metalofono')
parser.add_argument('-p', '--score', help='score')
parser.add_argument('-d', '--device', help='device')

args = parser.parse_args()
score= args.score
device= args.device
port=8080

notes = xilo_sheet_reader(score)
client = XyloClient(device, port)

if __name__ == '__main__':
    client.load(notes)
    client.play()