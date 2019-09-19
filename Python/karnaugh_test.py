import pytest
from karnaugh import *

def test_mintermToTruthTable():
    assert mintermToTruthTable(3, [0, 2, 3, 4, 6]) == [True, False, True, True, True, False, True, False]

def test_toCombination():
    assignations = [Assignation('a', True), Assignation('b', False), Assignation('c', True)]
    expected = Combination(set(assignations))
    actual = toCombination(['a', 'b', 'c'], 5)
    assert actual == expected