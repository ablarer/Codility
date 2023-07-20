# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # pass
    if len(A) == 0:
        return -1

    sort_a = sorted(A)
    l = len(A) // 2
    get_denominator = sort_a[l]
    number_of_denominator = sort_a.count(get_denominator)
    if number_of_denominator > l:
        return A.index(get_denominator)

print(solution([3, 4, 3, 2, 3, -1, 3, 3]))
