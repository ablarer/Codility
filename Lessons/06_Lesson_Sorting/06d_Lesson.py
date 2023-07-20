# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # pass
    N = len(A)
    left_edges = [0] * N
    right_edges = [0] * N

    for i in range(N):
        left_edges[i] = i - A[i]
        right_edges[i] = i + A[i]

    left_edges.sort()
    right_edges.sort()

    intersections = 0
    circles = 0

    j = 0
    for i in range(N):
        while j < N and right_edges[i] >= left_edges[j]:
            intersections += circles
            circles += 1
            if intersections > 10_000_000:
                return -1
            j += 1
        circles -= 1

    return intersections

print(solution([1, 5, 2, 1, 4, 0]))