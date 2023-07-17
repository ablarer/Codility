# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_version_1(A):
    # Implement your solution here
    # pass
    sorted_set_A = sorted(set(A))

    missing = 1

    for element in sorted_set_A:
        if element == missing:
            missing += 1
        elif element > missing:
            break

    return missing


def solution_version_2(A):
    # Firstly, sort all negative integers out.
    sorted_set_A = sorted(set(filter(lambda x: x > 0, A)))

    for i, element in enumerate(sorted_set_A):
        if element != i + 1:
            return i + 1

    # If no positive number is missing retunr the next higest
    return len(sorted_set_A) + 1

print(solution_version_2([-0]))
print(solution_version_2([-1]))
print(solution_version_2([0]))
print(solution_version_2([1]))
