# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math


def solution(A):
    # Implement your solution here
    # pass
    # Implement your solution here
    # pass
    length_array = len(A)
    total_sum = sum(A)
    left_sum = 0
    minimum = float('inf')

    for i in range(length_array - 1):
        left_sum += A[i]
        right_sum = total_sum - left_sum
        difference = abs(left_sum - right_sum)
        minimum = min(minimum, difference)

    return minimum

A = sum([1,2,3]) - sum([4,5,6])
print(A)

