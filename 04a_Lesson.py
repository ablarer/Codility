def solution(X, A):
    not_covered = [True] * X
    covered_count = 0

    for seconds, leaf in enumerate(A):
        if leaf <= X and not_covered[leaf - 1]:
            not_covered[leaf - 1] = False
            covered_count += 1
            print("Seconds: ", seconds, ", Leaf:", leaf, ", Covered: ", not_covered)
            if covered_count == X:
                return seconds

    return -1

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))