import pytest
from com.felipe.operacoes import Operacoes

def test_soma():
    operacoes = Operacoes()
    assert operacoes.func(1) == 2, "Should be 2"
