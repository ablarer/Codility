# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    from collections import Counter

    counts = Counter(A)

    for num in counts:
        if counts[num] == 1:
            return num

    return -1

print(solution([1, 3, 4, 3, 1, 2, 5]))

# You should find the first unique number in A. In other
# words, find the unique number with the lowest position in
# A.