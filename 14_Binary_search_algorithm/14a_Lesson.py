# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(K, M, A):
    # Implement your solution here
    # pass

    def check(mid, A, K):
        blocks = 1
        block_sum = 0

        for i in range(len(A)):
            if A[i] > mid:
                return False
            elif block_sum + A[i] > mid:
                block_sum = A[i]
                blocks += 1
                if blocks > K:
                    return False
            else:
                block_sum += A[i]

        return True

    start = max(A)
    end = sum(A)

    while start < end:
        mid = (start + end) // 2
        if check(mid, A, K):
            end = mid
        else:
            start = mid + 1

    return start

# M is not used for the solution.
print(solution(3, 5, [2, 1, 5, 1, 2, 2, 2]))