from cmath import isclose
from Sintetizador.functions import *

t = np.arange(0,1,0.1)

def test_constant():
    for i in t:
        assert constant(i, []) == 1

def test_linear():
    expected = t/2 
    for i, value in zip(t, expected):       
        assert linear(i, [2]) == value

def test_invlinear():
    assert invlinear(3, [2]) == 0
    assert invlinear(-1, [2]) > 0
    assert invlinear(0,[2]) > 0

def test_sin():
    assert sin(np.pi,[1,1]) > 1
    assert sin(np.pi/2, [1,1]) == 2

def test_exp():
    i = 0
    for ti in t:
        result = exp(ti,[2])
        assert result >= i   
        i = result

def test_invexp():
    i = 1
    for ti in t:
        result = invexp(ti,[2])
        assert result <= i   
        i = result

def test_quartcos():
    pass

def test_quartsin():
    pass

def test_halfcos():
    pass

def test_halfsin():
    pass

def test_log():
    i = 0
    for ti in t:
        result = log(ti,[2])
        assert result >= i   
        i = result

def test_invlog():
    i = 1
    for ti in t:
        result = invexp(ti,[2])
        assert result <= i   
        i = result
        
def test_tri():
    i = 0
    for ti in t:
        result = tri(ti,[1,1,1])
        assert result >= i   
        i = result
