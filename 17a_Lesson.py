def solution(A):
    N = len(A)
    max_result = [float('-inf')] * N
    max_result[0] = A[0]

    for i in range(N):
        for j in range(1, 7):
            if i + j < N:
                max_result[i + j] = max(max_result[i + j], max_result[i] + A[i + j])
                print("Field:", i, "Throw: ", j, "Sum: ", max_result[i + j])

    return max_result[N - 1]

print(solution([1, -2, 0, 9, -1, -2]))
