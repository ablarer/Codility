# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # Implement your solution here
    pass  # you can write to stdout for debugging purposes, e.g.


# print("this is a debug message")

def solution(A, B):
    # Implement your solution here

    result = ""

    while A > 0 or B > 0:

        if A > B:
            if result[-2:] != "aa":
                result += "a"
                A -= 1
            else:
                result += "b"
                B -= 1

        elif B > A:
            if result[-2:] != "bb":
                result += "b"
                B -= 1
            else:
                result += "a"
                A -= 1

        else:
            if result[-2:] == "aa":
                result += "b"
                B -= 1
            else:
                result += "a"
                A -= 1

    return result

print(solution(20, 2))