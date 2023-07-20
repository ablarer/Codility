# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(M, A):
    # Implement your solution here
    # pass

    array_length = len(A)
    total_slices = 0
    slice_start = 0
    # -1 for not yet seen elements
    last_occurrence = [-1] * (M + 1)

    for slice_end in range(array_length):
        # If element within our current slice not yet seen, adjust the start of the slice
        if last_occurrence[A[slice_end]] >= slice_start:
            slice_start = last_occurrence[A[slice_end]] + 1

        # Update the last occurrence of the element
        last_occurrence[A[slice_end]] = slice_end

        # Add the number of slices for the current window
        total_slices += slice_end - slice_start + 1

        if total_slices > 1e9:
            return int(1e9)

    return total_slices

print(solution(6, [3, 4, 5, 5, 2]))