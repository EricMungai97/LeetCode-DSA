import pytest
from leet_dsa.search_insert_postion import search_insert


def test_search_insert():
    nums = [1, 3, 5, 6]
    target = 5
    actual = search_insert(nums, target)
    expected = 2
    assert actual == expected
