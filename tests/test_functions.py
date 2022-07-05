from Sintetizador.functions import *

t = np.arange(0,1,0.1)
y = np.zeros(t.shape[0])

def test_constant():
    for i in t:
        assert constant(i, []) == 1

def test_linear():
    expected = t/2 
    for i, value in zip(t, expected):       
        assert linear(i, [2]) == value
        