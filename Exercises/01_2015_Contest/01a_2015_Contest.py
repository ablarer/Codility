# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    def is_valid_password(word):
        if not word.isalnum():
            return False

        letter_count = digit_count = 0
        for char in word:
            if char.isdigit():
                digit_count += 1
            elif char.isalpha():
                letter_count += 1

        # Check if there are an even number of letters and an odd number of digits
        return letter_count % 2 == 0 and digit_count % 2 == 1

    words = S.split()
    longest_valid_password = -1

    for word in words:
        if is_valid_password(word):
            longest_valid_password = max(longest_valid_password, len(word))

    return longest_valid_password

# Test example
S = "test 5 a0A pass007 ?xy1"
print(solution(S))  # Output: 7

