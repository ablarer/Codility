# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # Implement your solution here
    # pass
    block_count = 0
    stack = []

    for h in H:
        # Skip if stack is empty and
        # the top of the stack (stack[-1]) is not greater than the current height h.
        # Allows for removing elements from the stack that are higher than the current height
        while stack and stack[-1] > h:
            stack.pop()

        # Do not execute if
        # the stack is not empty (false) and
        # the top of the stack (stack[-1]) is equal to the current height (false)
        if not stack or stack[-1] != h:
            stack.append(h)
            print("Stack:", stack)
            block_count += 1

    return block_count

print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))