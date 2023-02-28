'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


'''


def longestCommonPrefix(strs):
    if not strs:
        return ""
    strs.sort()
    first = strs[0]
    last = strs[-1]

    common_prefix = ""
    for i in range(len(first)):
        if first[i] != last[i]:
            break
        common_prefix += first[i]
    return common_prefix

