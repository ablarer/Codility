# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # pass
    length_of_array  = len(A)
    sum_of_array = length_of_array * (length_of_array+ 1) // 2
    if sum(A) == sum_of_array and len(set(A)) == len(A):
        return 1
    return 0