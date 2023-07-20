# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_version_1(K, A):
    # Implement your solution here
    N = len(A)
    count = 0
    end = 0

    for start in range(N):
        while end < N and max(A[start:end+1]) - min(A[start:end+1]) <= K:
            end += 1
        count += end - start

        if count > 1_000_000_000:
            return 1_000_000_000

    return count

print(solution_version_1(2, [3, 5, 7, 6, 3]))


# Source
# https://stackoverflow.com/questions/21251707/counting-bounded-slice-codility
def solution_version_2(K, A):
# Implement your solution here
    def triangular(i):
        return (i * (i + 1)) // 2


    i = 0
    result = 0

    while i < len(A):
        lower = A[i]
        upper = A[i]
        countBackw = 0
        countForw = 0

        j = i - 1
        while j >= 0:
            if A[j] < lower:
                if upper - A[j] > K:
                    break
                else:
                    lower = A[j]
            elif A[j] > upper:
                if A[j] - lower > K:
                    break
                else:
                    upper = A[j]
            countBackw += 1
            j -= 1

        j = i
        while j < len(A):
            if A[j] < lower:
                if upper - A[j] > K:
                    break
                else:
                    lower = A[j]
            elif A[j] > upper:
                if A[j] - lower > K:
                    break
                else:
                    upper = A[j]
            countForw += 1
            j += 1

        result -= triangular(countBackw)
        result += triangular(countForw + countBackw)
        i += countForw

    return result

print(solution_version_2(2, [3, 5, 7, 6, 3]))
