# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    n = len(A)
    left_max = [0] * n
    right_max = [0] * n

    # Calculate the maximum height on the left of each position
    left_max[0] = A[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], A[i])

    # Calculate the maximum height on the right of each position
    right_max[n - 1] = A[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], A[i])

    maxDepth = 0

    # Calculate the depth at each position and update the maximum depth
    for i in range(1, n - 1):
        depth = min(left_max[i - 1], right_max[i + 1]) - A[i]
        if depth > 0:
            maxDepth = max(maxDepth, depth)

    return maxDepth

print(solution([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]))