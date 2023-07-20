# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A) == 1:
        return A[0]

    if len(A) == 0:
        return 0

    max_ending = 0
    max_slice = float('-inf')

    for num in A:
        max_ending = max(num, max_ending + num)
        max_slice = max(max_slice, max_ending)

    return max_slice


print(solution([3, 2, -6, 4, 0]))
print(solution([9]))
print(solution([]))
