from xylophone.xylo import XyloNote

def xilo_sheet_reader(filename):
        with open(filename, "r") as fd:  
            notes= ['G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 
            'E6', 'F6', 'G6', 'A6', 'B6', 'C7', 'G#4', 'Ab4', 'A#4', 'Bb4', 'C#5', 'Db5', 'D#5', 
            'Eb5', 'Ab5', 'A#5', 'Bb5', 'C#6', 'Db6', 'D#6', 'Eb6', 'F#6', 'Gb6', 'G#6', 'Ab6',
            'A#6', 'Bb6', 'C#7', 'Cb7']   
            xilo_allowed_notes= [] 
            velocity= 90
            a= fd.readlines()
            for line in a:
                line2= line.strip("\n").split(" ")
                start= line2[0]
                note= line2[1]
                if note in notes:
                    xiloNote= XyloNote(note,start,velocity)
                    xilo_allowed_notes.append(xiloNote)
            return xilo_allowed_notes