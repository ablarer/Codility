# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_version_1(A, B, K):
    count = 0
    for i in range(A, B + 1):
        if i % K == 0:
            count += 1
    return count

print(solution_version_1(6, 200, 2))

def solution_version_2(A, B, K):
    count = B // K - A // K
    print(A // K)
    print(B // K)
    if A % K == 0:
        count += 1
    return count

print(solution_version_2(6, 200, 2))