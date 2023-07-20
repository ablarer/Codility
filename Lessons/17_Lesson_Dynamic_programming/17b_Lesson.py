# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_version_1(A):
    # Implement your solution here
    # pass
    N = len(A)
    min_val = float('inf')

    # Iterate over all possible binary strings
    for i in range(2 ** N):
        # Generate the current binary string
        sequence = [1 if (i >> j) & 1 else -1 for j in range(N)]
        print(sequence)

        # Calculate the value of val(A, S)
        value = abs(sum(A[j] * sequence[j] for j in range(N)))

        # Update the minimum value if necessary
        min_val = min(min_val, value)

    # Return the final minimum value
    return min_val

print(solution_version_1([1, 5, 2]))

# Within the loop, the current binary string representing a sequence of 1s and -1s is generated.
# This is accomplished using bitwise operations.
# The loop variable i takes values from 0 to 2^N - 1, where N is the length of array A.
# Each value of i corresponds to a unique binary string.
# For example, if N = 3, the values of i will be 0, 1, 2, 3, 4, 5, 6, 7,
# representing all possible binary strings of length 3: 000, 001, 010, 011, 100, 101, 110, 111.
# To generate the current binary string, the digits of i are iterated over from right to left.
# For each digit position j in the range from 0 to N-1,
# the bitwise right shift operator >> and the bitwise AND operator & are used to extract the j-th digit from i.
# The expression (i >> j) & 1 shifts the bits of i to the right by j positions and
# then performs a bitwise AND operation with 1.
# This extracts the j-th digit from the binary representation of i.
# If the j-th digit is 1, the corresponding element in the sequence list is set to 1; otherwise, it is set to -1.
# By generating all possible binary strings in this manner,
# all combinations of multiplying the elements of array A by either 1 or -1 are explored,
# representing all possible sequences S that can be used to calculate val(A, S).

def solution_version_2(A):
    # Implement your solution here
    # pass
    total_sum = sum(A)
    min_val = float('inf')

    # Iterate over all possible subsets of A
    for i in range(1 << len(A)):
        subset_sum = 0
        for j in range(len(A)):
            if i & (1 << j):
                subset_sum += A[j]
        min_val = min(min_val, abs(total_sum - 2 * subset_sum))

    return min_val

print(solution_version_2([1, 5, 2]))