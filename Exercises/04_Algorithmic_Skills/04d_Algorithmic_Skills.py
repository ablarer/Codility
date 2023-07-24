def merge_and_count_inversions(left, right):
    # The two sorted arrays are merged while counting inversions.
    merged = []
    inversions = 0
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            # The number of inversions is incremented when an element in the right array is smaller than an element in the left array.
            inversions += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions


def merge_sort_and_count_inversions(arr):
    n = len(arr)
    # If the array has one element or is empty, it is considered sorted with zero inversions.
    if n <= 1:
        return arr, 0

    mid = n // 2
    # The left and right halves of the array are sorted and the inversions are counted for each subarray.
    left_half, left_count = merge_sort_and_count_inversions(arr[:mid])
    right_half, right_count = merge_sort_and_count_inversions(arr[mid:])
    merged, merge_count = merge_and_count_inversions(left_half, right_half)

    # The inversions from the left, right, and merge steps are combined to get the total number of inversions for the current array.
    total_count = left_count + right_count + merge_count
    return merged, total_count


def solution(A):
    # The array is sorted and the number of inversions is computed.
    _, inversions = merge_sort_and_count_inversions(A)

    # If the total number of inversions exceeds 1,000,000,000, the function returns -1.
    if inversions > 1000000000:
        return -1
    else:
        return inversions


# Example usage:
A = [-1, 6, 3, 4, 7, 4]
print(solution(A))  # Output: 4

# The merge_and_count_inversions function takes two sorted arrays (left and right) as input
# and merges them into a single sorted array while counting inversions.
# An inversion occurs when an element in the right array is smaller than an element in the left array.
# The merge_sort_and_count_inversions function is a recursive function that implements the merge sort algorithm.
# It divides the input array (arr) into halves until each subarray has one element or is empty.
# Then, it merges the sorted subarrays back together while counting the inversions in each merging step.
# In the merge_sort_and_count_inversions function, if the input array has one element or is empty (base case),
# it returns the array itself and 0 inversions since a single element or
# an empty array is considered sorted with no inversions.
# If the input array has more than one element, the function finds the midpoint of the array
# and recursively calls itself on the left and right halves of the array.
# The merge_and_count_inversions function is used during the merging step of the merge sort process.
# It takes two sorted arrays (left_half and right_half) and combines them into a single sorted array (merged)
# while counting the inversions that occur during the merging.
# The merge_and_count_inversions function uses two pointers i and j to iterate
# through the elements of the left_half and right_half arrays, respectively.
# It compares the elements pointed to by these pointers and appends the smaller element to the merged array.
# When an element from the right_half array is smaller than an element from the left_half array, an inversion is found.
# The number of inversions is then incremented by the number of remaining elements in the left_half array
# (since they are all greater than the current element in the right_half array).
# After merging the two halves, any remaining elements in either left_half or right_half are appended
# to the merged array.
# Finally, the merge_sort_and_count_inversions function combines the inversions from the left, right,
# and merge steps to get the total number of inversions for the current array.
# The solution function calls merge_sort_and_count_inversions on the input array A and
# returns the total number of inversions.
# If the total number of inversions exceeds 1,000,000,000, the function returns -1, as specified in the problem
# statement.
# In summary, the code uses a modified merge sort algorithm to efficiently count the number of inversions in the input
# array while performing the sorting process. The time complexity of the solution is O(N log N),
# making it efficient for large arrays.