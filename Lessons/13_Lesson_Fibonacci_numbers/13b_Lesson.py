# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # Implement your solution here
    # pass
    L = len(A)
    max_A = max(A)
    max_B = max(B)

    # Calculate the Fibonacci sequence up to max_A + 2
    fib = [0] * (max_A + 2)
    fib[1] = 1
    for i in range(2, max_A + 2):
        fib[i] = (fib[i - 1] + fib[i - 2]) % pow(2, max_B)

    # Calculate the number of ways for each value in A
    result = [0] * L
    for i in range(L):
        result[i] = fib[A[i] + 1] % pow(2, B[i])

    return result


print(solution([4, 4, 5, 5, 1], [3, 2, 4, 3, 1]))