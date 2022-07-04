from xylophone.xylo import XyloNote

def xilo_sheet_reader(filename):
        with open(filename, "r") as fd:      
            notesxilo= []
            velocity= 90
            a= fd.readlines()
            for line in a:
                line2= line.strip("\n").split(" ")
                start= line2[0]
                note= line2[1]
                xiloNote= XyloNote(note,start,velocity)
                notesxilo.append(xiloNote)
            return notesxilo


