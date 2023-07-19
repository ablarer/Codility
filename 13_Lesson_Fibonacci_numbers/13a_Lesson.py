# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
     #pass

        N = len(A)

        # Add an extra leaf on the other bank
        A.append(1)

        # Generate the Fibonacci sequence up to N+2
        fibonacci = [0, 1]
        while fibonacci[-1] <= N + 1:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])

        # Remove the unnecessary first two Fibonacci numbers
        fibonacci = fibonacci[2:]

        # Initialize the dynamic programming array
        dp = [-1] * (N + 1)

        # Calculate the minimum number of jumps to each position
        for i in range(N + 1):
            if A[i] == 0:
                continue

            for fib in fibonacci:
                if fib - 1 == i:
                    dp[i] = 1
                elif fib - 1 < i and dp[i - fib] != -1:
                    if dp[i] == -1 or dp[i - fib] + 1 < dp[i]:
                        dp[i] = dp[i - fib] + 1

        return dp[N]


A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
print(solution(A))

