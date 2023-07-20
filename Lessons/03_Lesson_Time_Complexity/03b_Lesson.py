# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # pass

    # Sum of the arithmetic series with N numbers.
    # (N) * (N + 1) / 2
    # e.g., 1 to 10 with no missing number: N = 10, N + 1 / 2 = 5.5
    # -> 10 * 5.5 = 55

    # Sum of the arithmetic series with N - 1 numbers:
    # (N + 1) * (N + 2) / 2
    # e.g., 1 to 10 with one missing number: N = 9, N + 1 = 10, N + 2 / 2 = 5.5
    # -> 10 * 5.5 = 55

    expected_sum = (len(A) + 1) * (len(A) + 2) // 2
    print("Expected sum: ", expected_sum)

    # Calculate the actual sum of elements in the array
    actual_sum = sum(A)
    print("Acutal sum: ", actual_sum)

    # The missing element is the difference between the expected sum and the actual sum
    missing_element = expected_sum - actual_sum

    return missing_element

print(solution([1,2,3,4,6,7,8,9,10]))
print(solution([10, 9, 3, 8, 4, 7, 2, 1, 6]))
print(solution([2, 3, 1, 5]))
print(solution([1]))