from Packages.note import Note
import numpy as np

test_note = Note("A4", '440.000', '1.0', '0.0')
    
def test_get_duration():
    assert test_note.get_duration() == 1.0

def test_get_frecuency():
    assert test_note.get_frecuency() == 440.000
    
def test_get_start():
    assert test_note.get_start() == 0.0   
    
def test_get_sinuoidal():
    t = np.arange(test_note.get_start(), test_note.get_start() + test_note.get_duration(), 1/44100)
    y = np.sin(np.pi*test_note.get_frecuency()*t) 
    test_note.set_sinuoidal(t, y)
    assert np.array_equal(test_note.get_sinuoidal()[0], t)
    assert np.array_equal(test_note.get_sinuoidal()[1], y)
    
