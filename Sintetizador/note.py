from __future__ import annotations
from typing import Tuple
import numpy as np

class Note(object):
    def __init__ (self, name: str, frecuency: str, duration: str, start: str) -> None:
        self.name= name
        self.frecuency= float(frecuency)
        self.duration= float(duration)
        self.start= float(start)
        self.sinuoidal = None

    def get_frecuency(self) -> float:
        """
        param self: Access the attributes and methods of the class in python
        return: The frequency of the note
        """
        return self.frecuency

    def get_duration(self) -> float:
        """
        The get_duration function returns the duration of a note.
        
        param self: Refer to the object itself
        return: The duration of the note
        """
        return self.duration
    
    def get_start(self) -> float:
        """
        The get_start function returns the start position of the current note.
        
        param self: Access the attributes and methods of the class in python
        return: start point of the note
        """
        return self.start
    
    def set_sinuoidal(self, t: np.array, y: np.array) -> None:
        """
        The set_sinuoidal function sets the waveform to a sinusoidal wave.
        
        param self: Access variables that belongs to the class
        param t: Set the time of the sinuoidal function
        param y: Set the amplitude of the sinuoidal function
        return: A list of tuples
        """
        self.sinuoidal = t,y
    
    def get_sinuoidal(self) -> Tuple[np.array|np.array]:
        """
        The get_sinuoidal function returns a sinuoidal function with the given parameters.
        
        param self: Refer to the object that will be calling the function
        return: A sinuoidal function with a frequency of 1/2
        """
        return self.sinuoidal

    def __eq__(self, note: Note) -> bool:
        """
        The __eq__ function checks if the start and duration of two notes are equal.
        It returns True if they are, False otherwise.
        
        param self: Refer to the current object
        param note:Note: Check if the note is of type note
        return: A boolean value
        """
        if isinstance(note,Note):
            if (note.get_start() == self.get_start()) and (note.get_duration() == self.get_duration()):
                return True
        return False

    def __str__(self) -> str:
        """
        The __str__ function is called when an instance of the class is printed. 
        
        param self: Refer to the object itself
        return: The string representation of the object
        """
        return (f'{self.name},{self.frecuency}, {self.start}, {self.duration}')
    
    def __gt__(self, note: Note) -> bool:
        """
        The __gt__ function compares the start time of two notes. If the first note's start time is greater than 
        the second note's, then True is returned. If they are equal, it checks if the duration of the first note is 
        greater than that of the second and returns True or False accordingly.
        
        param self: Refer to the object itself
        param note:Note: Compare the start time of two notes
        return: A boolean value
        """
        if isinstance(note, Note):
            if self.get_start() > note.get_start():
                return True
            elif self.get_start() == note.get_start():
                if self.get_duration() > note.get_duration():
                    return True
        return False
    
    def __lt__(self, note: Note) -> bool:
        """
        The __lt__ function compares the start time of two notes. If the first note's start time is less than 
        the second note's, then it returns True. Otherwise, if they are equal or if the first note's start time is 
        greater than that of the second, it returns False.
        
        param self: Refer to the object itself
        param note:Note: Compare the start time of two notes
        return: A boolean value
        """
        if isinstance(note, Note):
            if self.get_start() < note.get_start():
                return True
            elif self.get_start() == note.get_start():
                if self.get_duration() < note.get_duration():
                    return True
        return False           
    def __repr__(self) -> str:
        """        
        param self: Refer to the instance of the class
        return: The string representation of the object
        """
        return self.name