import pytest
from leet_dsa.longest_common_prefix import longestCommonPrefix
def test_longest_common_prefix():
    strs = ["flower", "flow", "flight"]
    actual = longestCommonPrefix(strs)
    expected = "fl"
    assert actual == expected


