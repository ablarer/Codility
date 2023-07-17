# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import itertools

def solution(A):
    # Implement your solution here
    # pass
    N = len(A)
    min_val = float('inf')

    for S in itertools.product([-1, 1], repeat=N):
        val = sum(A[i] * S[i] for i in range(N))
        min_val = min(min_val, abs(val))

    return min_val

print(solution([1, 5, 2, -2]))