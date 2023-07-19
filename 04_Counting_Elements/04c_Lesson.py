# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # Implement your solution here
    # pass
    counters = [0] * N
    maximum_counter = 0
    last_maximum_counter = 0

    for operation in A:
        if 1 <= operation <= N:
            if counters[operation - 1] < last_maximum_counter:
                counters[operation - 1] = last_maximum_counter
            counters[operation - 1] += 1
            if counters[operation - 1] > maximum_counter:
                maximum_counter = counters[operation - 1]
        elif operation == N + 1:
            last_maximum_counter = maximum_counter

    for i in range(N):
        if counters[i] < last_maximum_counter:
            counters[i] = last_maximum_counter

    return counters