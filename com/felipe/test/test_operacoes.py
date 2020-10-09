import pytest
from com.felipe.operacoes import *

def func(x):
    return x + 1

def test_soma():
    assert func(3) == 4
