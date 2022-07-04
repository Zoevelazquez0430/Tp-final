import pytest
import principal_file as note
import funciones
import test_instrumento_1 as inst_1
nota=note.Note("name", 1000, 10, 0)

def test_instrumento():
    c=nota.instrumento(inst_1)
    return c

#test_sintetizador():
  #  note.
    

#test_notes()