# Source:
# https://codesays.com/2016/solution-to-slalom-skiing-by-codility/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # Helper function to prepare the input array A as required
    def create_array(A):
        maxA = max(A) + 1
        modified_A = []
        for i in A:
            # Append three values for each element in A:
            # 1. 2 * maxA + i
            # 2. 2 * maxA - i
            # 3. i
            # This step helps in later processing to find the longest increasing subsequence.
            modified_A.append(2 * maxA + i)
            modified_A.append(2 * maxA - i)
            modified_A.append(i)
        return modified_A

    # Helper function to find the length of the longest increasing subsequence
    def find_best_list(A):
        M = []
        for i in A:
            j = len(M)
            # Perform a binary search to find the appropriate position to insert the current element i in M.
            while j > 0 and M[j - 1] >= i:
                j -= 1
            # If j equals the length of M, the current element is greater than all elements in M.
            # Hence, extend M by appending the current element.
            if j == len(M):
                M.append(i)
            # If j is less than the length of M, the current element is smaller than an element in M.
            # Replace M[j] with the current element, as this would lead to a potentially longer subsequence.
            else:
                M[j] = i
        # Return the length of the longest increasing subsequence (length of M).
        return len(M)

    # Create the modified array using create_array, and find the longest increasing subsequence length using find_best_list.
    return find_best_list(create_array(A))


# Test example
A = [15, 13, 5, 7, 4, 10, 12, 8, 2, 11, 6, 9, 3]
print(solution(A))  # Output: 8

