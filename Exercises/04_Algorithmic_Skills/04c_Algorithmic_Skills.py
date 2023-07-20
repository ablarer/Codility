# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# from extratypes import Tree  # library with types used in the task

def solution(T):
    # Implement your solution here
    if T is None:
        # Empty tree has height -1
        return -1

    left_height = solution(T.l)
    right_height = solution(T.r)

    return max(left_height, right_height) + 1


T = Tree(5, Tree(3, Tree(20), Tree(21)), Tree(10, Tree(1)))
print(solution(T))