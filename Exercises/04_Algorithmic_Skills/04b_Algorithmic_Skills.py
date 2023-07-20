# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    left = 0
    right = len(S) - 1

    while left < right:
        if S[left] == S[right]:
            # Move the pointers inward
            left += 1
            right -= 1
        else:
            # Substrings are not reversals, return -1
            return -1

        print("Left:", left)
        print("Right:", right)

    # Check if the length is odd and return the index
    if left == right:
        return left

    # String is a complete reversal, return -1
    return -1

print(solution('racecar'))