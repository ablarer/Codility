# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from math import sqrt

def solution(N, P, Q):
    # Implement your solution here
    # pass
    sieve = [0] * (N + 1)
    prefix_sum = [0] * (N + 1)
    semiprime_count = 0

    # Generate semiprime counts
    for i in range(2, int(sqrt(N))  + 1):
        if sieve[i] == 0:
            for j in range(i * i, N + 1, i):
                if sieve[j] == 0:
                    sieve[j] = i

    for i in range(2, N + 1):
        if sieve[i] != 0 and sieve[i // sieve[i]] == 0:
            semiprime_count += 1
        prefix_sum[i] = semiprime_count

    result = []
    for i in range(len(P)):
        count = prefix_sum[Q[i]] - prefix_sum[P[i] - 1]
        result.append(count)

    return result

print(solution(26, [1, 4, 16], [26, 10, 20]))