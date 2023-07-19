# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    # pass
    factors = []
    i = 1
    while i * i <= N:
        if N % i == 0:
            factors.append(i)
            if i != N // i:  # Avoid adding duplicates for perfect square numbers
                factors.append(N // i)
        i += 1
    return len(factors)


print(solution(24))
print()
print(solution(16))
print()
print(solution(2479))