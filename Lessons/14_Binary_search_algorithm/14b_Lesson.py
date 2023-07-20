# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C):
    # Implement your solution here
    # pass

    planks = sorted(list(zip(A, B)))

    def check(mid):
        nails = sorted(C[:mid])
        j = 0

        for nail in nails:
            while j < len(planks) and planks[j][0] <= nail <= planks[j][1]:
                j += 1
            if j == len(planks):
                return True
        return False

    # Using at least one nail (1) and using all nails (len(C) + 1)
    lower, upper = 1, len(C) + 1
    result = -1
    while lower < upper:
        mid = (lower + upper) // 2
        if check(mid):
            upper = mid
            result = mid
        else:
            lower = mid + 1

    print("Planks:\t", *planks)
    print("Nails:\t", *C)
    return result

print(f"You need {solution([1, 4, 5, 8], [4, 5, 9, 10], [4, 6, 7, 10, 2])} nails.")