# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # pass
    N = len(A)
    A.sort()
    count = 0
    for P in range(N):
        R = P + 2
        for Q in range(P + 1, N):
            while R < N and A[P] + A[Q] > A[R]:
                R += 1
            count += max(0, R - Q - 1)
    return count

print(solution([10, 2, 5, 1, 8, 12]))