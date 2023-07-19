def solution(A, B):
    stack = []
    remaining_fish = 0

    for i in range(len(A)):
        if B[i] == 0:
            while stack and A[i] > stack[-1]:
                stack.pop()

            if not stack:
                remaining_fish += 1
        else:
            stack.append(A[i])

    return remaining_fish + len(stack)

if __name__ == '__main__':
    assert solution([4,3,2,1,5], [0,1,0,0,0]) == 2