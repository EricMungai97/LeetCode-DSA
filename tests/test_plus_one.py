from leet_dsa.plusone import plusOne
import pytest

def test_plusOne_list_with_multiple_elements():
    digits = [1,2,3,4]
    actual = plusOne(digits)
    expected = [1,2,3,5]
    assert actual == expected

def test_plusOne_list_with_9_as_last_element():
    digits = [1,9,9,9]
    actual = plusOne(digits)
    expected = [2,0,0,0]
    assert actual == expected
