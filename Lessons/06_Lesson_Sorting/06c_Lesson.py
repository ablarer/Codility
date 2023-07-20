# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # pass
    if len(A) <= 2:
        return 0

    A.sort()

    for i in range(0, len(A) - 2):
        if A[i] + A[i+1] > A[i+2]:
            return 1

    return 0

print(solution([10, 2, 5, 1, 8, 20]))
print(solution([10, 50, 5, 1]))