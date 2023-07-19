# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(N):
    # Implement your solution here
    # pass
    min_perimeter = float('inf')
    sqrt_N = int(math.sqrt(N))

    for i in range(1, sqrt_N + 1):
        if N % i == 0:
            factor_1 = i
            factor_2 = N // i
            perimeter = 2 * (factor_1 + factor_2)
            min_perimeter = min(min_perimeter, perimeter)

    return min_perimeter

print(solution(32))