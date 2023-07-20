# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Caterpillar method
# The caterpillar method is a simplified version of the two-pointer technique.
def solution(A):
    # The input array A is sorted in ascending order.
    A.sort()
    N = len(A)

    # Two pointers, 'front' and 'back', are initialized at the beginning and end of the array, respectively.
    front, back = 0, N - 1
    # A variable 'min_abs_sum' is initialized to hold the minimum absolute sum. It is initially set to infinity.
    min_abs_sum = float('inf')

    # A while loop is run until 'front' is less than or equal to 'back'.
    while front <= back:
        # For each iteration, the sum of the elements pointed by 'front' and 'back' is computed.
        cur_sum = A[front] + A[back]
        # If the absolute value of this sum is smaller than 'min_abs_sum', 'min_abs_sum' is updated with this new value.
        min_abs_sum = min(min_abs_sum, abs(cur_sum))

        # If the current sum is less than or equal to zero, the 'front' pointer is incremented by 1.
        # This is done to increase the sum, since the array is sorted and elements towards the right are larger.
        if cur_sum <= 0:
            front += 1
        # If the current sum is greater than zero, the 'back' pointer is decremented by 1.
        # This is done to decrease the sum, since elements towards the left are smaller.
        else:
            back -= 1

    # After the loop, 'min_abs_sum' is returned as the smallest absolute sum of any pair in the array.
    return min_abs_sum

print(solution( [1, 4, -3]))
print(solution( [-8, 4, 5, -10, 3]))