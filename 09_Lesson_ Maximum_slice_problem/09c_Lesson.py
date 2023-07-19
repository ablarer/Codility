# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    pass
    N = len(A)
    max_ending = [0] * N
    max_starting = [0] * N
    max_double_slice = [0] * N

    for i in range(1, N - 1):
        print(max_ending)
        max_ending[i] = max(0, max_ending[i - 1] + A[i])

    print()

    for i in range(N - 2, 1, -1):
        print(max_starting)
        max_starting[i] = max(0, max_starting[i + 1] + A[i])

    print()

    for i in range(1, N - 1):
        print(max_double_slice)
        max_double_slice[i] = max(max_ending[i - 1] + max_starting[i + 1], max_double_slice[i - 1])

    return max(max_double_slice)

print(solution([3, 2, 6, -1, 4, 5, -1, 2]))