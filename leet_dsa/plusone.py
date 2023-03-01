
def plusOne(digits):
    n = len(digits)
    i = n - 1
    while i >= 0 and digits[i] == 9:
        i -= 1
    if i == -1:
        return [1] + [0] * n
    digits[i] += 1
    for j in range(i + 1, n):
        digits[j] = 0
    return digits