from __future__ import annotations
import wave
from matplotlib import pyplot as plt
import numpy as np
from note import Note
from notes import notes_mapping
from typing import List, Tuple
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
from functions import *

class Sintetizer():
    def __init__(self, sample_rate: int,  instrument: str, score: str, wave_file) -> None:
        self.sample_rate = int(sample_rate)
        self.instrument_info = instrument
        self.sheet= score
        self.wave_file= wave_file
        self.notes_list= []
        self.attack_t = None
        self.decay_t = None
        self.functions = []
    
    def set_times(self, attack_t, decay_t):
        """
        The set_times function sets the attack and decay times for the envelope.
        
        Args:
            attack_t (float): The time in seconds of the envelope's attack phase. 
            decay_t (float): The time in seconds of the envelope's decay phase. 
        
        
        param self: Access the variables and methods of the class in python
        param attack_t: Set the time it takes for the sound to reach its maximum volume
        param decay_t: Set the duration of the decay phase
        return: The attack_t and decay_t parameters
        """
        self.attack_t, self.decay_t = attack_t, decay_t

    def instrument(self, filename: str) -> Tuple[List]:
        """
        The instrument function takes a filename as an argument and returns the attack time, decay time, 
        and list of intensities. The function also creates a list of functions that will be used to create 
        the waveforms.
        
        param self: Access variables that belongs to the class
        param filename:str: Specify the name of the file containing the function information
        return: A tuple that contains a list of intensities and a list of times
        """
        contador = 0
        with open(filename, "r") as fd:
            function_info={} 
            intensities= []
            multiples=[]
            a= fd.readlines()
            a.pop(0)
            for line in a:
                line2= line.strip("\n").split(" ")
                if line2[0].isnumeric():
                    multiple= float(line2[1])
                    intensities.append(multiple)
                    multiples.append(int(line2[0]))
                else:
                    a=[]
                    for i in range (1,len(line2)):
                        line2= line.strip("\n").split(" ")
                        a.append(float(line2[i]))
                    function_info[line2[0]]= a
            for function in function_info:
                contador += 1
                if contador == 1:
                    attack_t = function_info[function][0]
                elif contador == 3:
                    decay_t = function_info[function][0]
                self.functions.append(function)
            self.set_times(attack_t, decay_t)
            return multiples, intensities, function_info 

    def modulator(self,t, y, functions, note ):
        """
        The modulator function takes in a time vector, a function vector, and an instrument object. It then uses the 
        instrument's attack_t and decay_t attributes to create an envelope for the given note. The envelope is created by 
        using three functions from the dictionary dic: CONSTANT, LINEAR,
        
        param self: Access variables that belongs to the class
        param t: Generate the time vector
        param y: Store the values of the function that we want to plot
        param functions: Pass the parameters of each function
        param note: Get the start time of the note and its duration
        return: A vector of values for the given function
        """
        dic = {"CONSTANT": constant, "LINEAR": linear,"INVLINEAR":invlinear , "SIN": sin, "EXP": exp, "INVEXP": invexp,
         "QUARTCOS": quartcos, "QUARTSIN": quartsin, "HALFCOS": halfcos, "HALFSIN": halfsin, "LOG": log, "INVLOG": invlog,
          "TRI": tri,"PULSES":pulses}
        m = np.zeros(t.shape[0])
        t_start = note.get_start()
        duration = note.get_duration()

        for i, ti in enumerate(t):
            if  t_start < ti < t_start + self.attack_t:
                m[i] = dic[self.functions[0]](ti-t_start, functions[self.functions[0]])
            if t_start + self.attack_t < ti < t_start + duration:
                m[i] = dic[self.functions[1]](ti-(t_start + self.attack_t), functions[self.functions[1]])
            if t_start + duration < ti < t_start + duration + self.decay_t:
                m[i] = dic[self.functions[1]](t_start + duration, functions[self.functions[1]]) * dic[self.functions[2]](ti-(t_start + duration), functions[self.functions[2]])

        return m

    def sintthesize(self):
        """
        The sintthesize function synthesizes the notes in the list of Note objects.
        It uses a sinusoidal waveform generator to create each note and then adds them together.
        The function returns a tuple containing two arrays: one for time, and another for amplitude.
        
        param self: Access variables that belongs to the class
        return: The sum of the sinuoidal signals
        """
        multiples, intensities = self.instrument(self.instrument_info)
        self.notes_maker()
        y2 = None
        for note in self.notes_list:
            y,t = self.sonador(note, multiples, intensities)
            note.set_sinuoidal(t,y)
            print(note)
            y2 += y
        
    def add_sinu(self) -> None:
        """
        The add_sinu function adds a sinusoidal wave to the signal.
        
        Parameters:
            multiples (list): A list of integers that represent the number of times 
                each note is played. For example, if multiples = [2, 3], then every 
                other note will be repeated twice and every
        
        param self: Access variables that belongs to the class
        return: None
        """
        multiples, intensities, functions = self.instrument(self.instrument_info)
        self.notes_maker()
        for note in self.notes_list:
            t, y = self.sinu_maker(note, multiples, intensities, functions)
            note.set_sinuoidal(t,y)
    
    def sinu_maker(self, note: Note, multiples: List[float], intensities: List[float], functions):
        """
        The sinu_maker function creates a sinusoidal waveform with the given parameters.
        It takes in a note, and multiplies it by different sinusoidal functions of varying frequency.
        The output is then multiplied by an envelope function to create the final waveform.
        
        param self: Access the attributes and methods of the class in python
        param note:Note: Get the note frequency and start time of the sinusoidal signal
        param multiples:List[float]: Define the frequencies of the sinusoidal waves that are going to be summed
        param intensities:List[float]: Set the intensity of each sinusoidal component
        param functions: Apply a function to the signal
        return: A numpy array of the sinusoidal waves that are going to be added to the signal
        """
        F0= note.get_frecuency()
        Ts= 1/self.sample_rate
        t= np.arange(note.get_start(),note.get_start()+note.get_duration()+self.decay_t, Ts)
        y= np.zeros(len(t))
        for multi, inten in zip(multiples, intensities):
            y+=inten*np.sin(2*np.pi*multi*F0*t)
        y= self.modulator(t, y, functions, note)* y
        y = y*0.07
        return t, y

    def read_sheet(self, filename: str) -> List[Tuple]:
        """
        The read_sheet function reads a file and returns a list of tuples containing the start time, end time, and note name for each note in the file.
        
        param self: Access variables that belong to the class (e
        param filename:str: Specify the name of the file that contains the sheet
        return: A list of tuples
        """
        with open(filename, "r") as fd:      
            notas= []
            a= fd.readlines()
            for line in a:
                line2= line.strip("\n").split(" ")
                comienzo= line2[0]
                note= line2[1]
                duración= line2[2]
                if float(duración)> 0:
                    notas.append((comienzo,note,duración))
            return notas

    def notes_maker(self) ->None:
        """
        The notes_maker function prints out the notes in a list of tuples.
           The function takes no parameters and returns nothing.
        
        param self: Access variables that belongs to the class
        return: None
        """
        notas = self.read_sheet(self.sheet)
        for note in notas:
            NOTA = Note(note[1], self.notes_finder(note), note[2], note[0])
            self.notes_list.append(NOTA)
        self.notes_list.sort()
    
    def notes_finder(self, note: Note) -> float:
        """
        The notes_finder function takes a Note object as an argument and returns the corresponding frequency.
        
        param self: Access the attributes and methods of the class
        param note:Note: Indicate the note that we want to find in the dictionary
        return: The frequency of the note that is passed as a parameter
        """
        for nom,frec in notes_mapping:
                if note[1]==nom:
                    return frec
    
    def total_duration(self) -> float:
        """
        The total_duration function returns the total duration of a NoteList object.
        
        param self: Access the attributes and methods of the class in python
        return: The total duration of the instrument
        """
        duration = 0
        for note in self.notes_list:
            aux_duration = note.get_start() + note.get_duration() + self.decay_t
            if aux_duration > duration:
                duration = aux_duration
        return duration

    def generate_track(self, file_to_make, sample_rate):
        """
        The generate_track function generates a track from the list of notes.
        It adds all the sinuosities and then it sums them up.
        
        param self: Access variables that belongs to the class
        return: A tuple with the time and the wave
        """
        self.add_sinu()
        t = np.arange(0, self.total_duration(), 1/self.sample_rate)
        y = np.zeros(len(t))

        for note in self.notes_list:
            t_nota, y_nota = note.get_sinuoidal()
            index_inicio = np.where(np.isclose(t, t_nota[0],(1/self.sample_rate), 1/self.sample_rate))[0][0]
            y[index_inicio : index_inicio + len(y_nota)] += y_nota

        write(file_to_make, int(sample_rate), y)
