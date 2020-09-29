# Både övning 42 och 43. Testar funktioner i bägge.

from Ovning39 import count
from Övning40 import rev_text, big_L

'''
def test_max():
    expected = 3
    got = count(1, 2, 3)
    assert expected == got
'''
'''
# Testar 40.1
def test_rev_text1():
    expected = "12345"

    assert rev_text(expected) == "54321"

def test_rev_text2():
    expected = "12345"
    assert  rev_text(expected) != "12345"

def test_rev3():
    expected = "12345"
    assert rev_text(expected) == "12345"
'''

def test_bigL():
    expected = "TjoHejSANAlla"
    assert big_L(expected) != 4
