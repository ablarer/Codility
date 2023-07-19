def solution(A, B):
    N = len(A)
    if N == 0:
        return 0

    count = 1
    prev_end = B[0]

    for i in range(1, N):
        if A[i] > prev_end:
            print(f"A: {i}, pre_end: {prev_end}")
            count += 1
            prev_end = B[i]

    return count

print(solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10]))