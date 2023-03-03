from leet_dsa.remove_dups_sorted_array import remove_duplicates

def test_remove_duplicates():
    nums = [1,1,2]
    actual = remove_duplicates(nums)
    expected = 2
    assert actual == expected
