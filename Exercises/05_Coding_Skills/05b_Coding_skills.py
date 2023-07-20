# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    highest_power = 0

    # Divide N by 2 until it becomes odd
    while N % 2 == 0:
        N = N // 2
        highest_power += 1

    return highest_power

print(solution(28))