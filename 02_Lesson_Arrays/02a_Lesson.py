# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here
    # pass
    length_array = len(A)

    if length_array == 0:
        return A

    K = K % length_array
    A[:] = A[length_array - K:] + A[:length_array - K]

    return A

print(solution([1,2,3,4,5,6,7,8,9,10], 2))