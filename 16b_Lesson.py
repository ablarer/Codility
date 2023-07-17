# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, A):
    # Implement your solution here
    # pass
    N = len(A)
    count = 0
    current_length = 0

    for i in range(N):
        current_length += A[i]
        if current_length >= K:
            count += 1
            current_length = 0

    return count

print(solution(4, [1, 2, 3, 4, 1, 1, 3]))