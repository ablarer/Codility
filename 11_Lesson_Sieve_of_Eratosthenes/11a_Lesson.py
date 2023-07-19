# Source:
# https://github.com/Dineshkarthik/codility-training/blob/master/Lesson%2011%20-%20Sieve%20of%20Eratosthenes/count_not_divisible.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # pass

    _dict = {}
    maxA = 0

    for a in A:
        _dict[a] = _dict.get(a, 0) + 1  # count repetitions
        maxA = max(a, maxA)
    ND = [len(A) - 1] * (maxA + 1)

    for b in _dict.keys():
        ND[b] -= (_dict[b] - 1)
        m = b * 2
        while m <= maxA:
            ND[m] -= _dict[b]
            m += b
    result = []

    for a in A:
        result += [ND[a]]

    return result

print(solution([3, 1, 2, 3, 6]))