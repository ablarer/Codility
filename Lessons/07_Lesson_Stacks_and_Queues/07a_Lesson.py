# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    # pass
    stack = []

    for bracket in S:
        if bracket in ('(', '{', '['):
            stack.append(bracket)

        elif bracket in (')', '}', ']'):
            if not stack:
                return 0

            top = stack.pop()
            if (bracket == ')' and top != '(') or \
               (bracket == '}' and top != '{') or \
               (bracket == ']' and top != '['):
               return 0

    return 1 if not stack else 0

print(solution('{[()()]}'))
print(solution('([)()]'))