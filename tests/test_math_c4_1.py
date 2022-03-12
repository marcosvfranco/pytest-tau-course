import pytest

def test_multiply_two_positive_ints():
    assert 2*3 == 6

def test_multiply_identity():
    assert 1*99 == 99

def test_multiply_zero():
    assert 0 * 100 == 0

#DRY Principle: Dont repeate yourself