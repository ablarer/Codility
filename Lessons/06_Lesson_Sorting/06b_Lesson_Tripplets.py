# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from functools import reduce
from itertools import combinations


def solution_version_1(A):
    # Implement your solution here
    # pass
    triplets = []
    for triplet in combinations(A, 3):
        triplets.append(triplet)

    triplet_products = []
    for triplet in triplets:
        product = reduce(lambda x, y: x * y, triplet)
        triplet_products.append(product)

    return max(triplet_products)

print(solution_version_1([-3, 1, 2, -2, 5, 6]))

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_version_2(A):
    # Implement your solution here
    # pass
    sorted_A = sorted(A)
    product_max_1 = sorted_A[-1] * sorted_A[-2] * sorted_A[-3]
    product_max_2 = sorted_A[0] * sorted_A[1] * sorted_A[-1]
    return max(product_max_1, product_max_2)

print(solution_version_2([-3, 1, 2, -2, 5, 6]))