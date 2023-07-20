# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    # pass
    N = bin(N).strip("0b")

    print(N)

    zero_sequences = N.split('1')

    max_zeros = max(len(seq) for seq in zero_sequences)

    return max_zeros

decimal_number = 28700  # Example decimal number
largest_zeros = solution(decimal_number)
print(f"Largest consecutive zeros: {largest_zeros}")

