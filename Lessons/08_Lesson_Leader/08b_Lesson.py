# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    pass
    stack = []
    for num in A:
        if not stack or stack[-1] == num:
            stack.append(num)
        else:
            stack.pop()

    if not stack:
        return 0

    leader = stack[-1]
    leader_count = A.count(leader)
    if leader_count <= len(A) // 2:
        return 0

    equi_leaders = 0
    leader_count_so_far = 0
    for i in range(len(A)):
        if A[i] == leader:
            leader_count_so_far += 1
        if leader_count_so_far > (i + 1) // 2 and leader_count - leader_count_so_far > (len(A) - i - 1) // 2:
            equi_leaders += 1

    return equi_leaders

print(solution([4, 3, 4, 4, 4, 2]))