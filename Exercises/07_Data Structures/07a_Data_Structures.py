# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    length = 0
    current = 0

    while current != -1:
        current = A[current]
        length += 1

    return length

print(solution([1, 4, -1, 3, 2]))