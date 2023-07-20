# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # pass
    plus_signed_A = []
    for n in A:
        plus_signed_A.append(abs(n))

    set_A = set(plus_signed_A)

    return len(set_A)

print(solution([-5, -3, -1, 0, 3, 6]))