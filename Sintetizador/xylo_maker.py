from fileinput import filename
from xylophone.xylophone.client import XyloClient
from xylo_reader import xilo_sheet_reader

notes = xilo_sheet_reader("gravity_falls.txt")

client = XyloClient(host='localhost', port=8080)
client.load(notes)
client.play()