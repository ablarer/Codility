# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    arr = list(S)
    length = len(arr)
    write_index = 0

    for read_index in range(length):
        if write_index > 0 and arr[read_index] == arr[write_index - 1]:
            # Found a pair of consecutive characters that can be removed
            write_index -= 1
        else:
            # Keep the current character since no transformation can be applied
            arr[write_index] = arr[read_index]
            write_index += 1

    return ''.join(arr[:write_index])


# Test cases
print(solution("ACCAABBC"))  # Output: "AC"
print(solution("ABCBBCBA"))  # Output: ""
print(solution("BABABA"))  # Output: "BABABA"