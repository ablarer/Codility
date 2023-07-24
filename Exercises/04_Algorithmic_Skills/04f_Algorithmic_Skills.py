from dataclasses import dataclass, field
import math

@dataclass
class Point2D:
    x: int
    y: int

def polar_angle(point, ref_point):
    return math.atan2(point.y - ref_point.y, point.x - ref_point.x)

def left_turn(p1, p2, p3):
    return (p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y) >= 0

def graham_scan(points):
    n = len(points)
    if n <= 3:
        return points

    # Find the reference point (lowest y-coordinate, leftmost in case of a tie)
    ref_point = min(points, key=lambda p: (p.y, p.x))

    # Sort the points based on their polar angles with respect to the reference point
    sorted_points = sorted(points, key=lambda p: polar_angle(p, ref_point))

    # Build the convex hull using a stack
    stack = [sorted_points[0], sorted_points[1]]
    for i in range(2, n):
        while len(stack) >= 2 and not left_turn(stack[-2], stack[-1], sorted_points[i]):
            stack.pop()
        stack.append(sorted_points[i])

    return stack

def solution_version_1(A):
    convex_hull = graham_scan(A)

    for i, point in enumerate(A):
        if point not in convex_hull:
            return i

    # If all points in the original array are part of the convex hull, return -1
    return -1

# Test cases
print(solution_version_1([
    Point2D(-1, 3),
    Point2D(1, 2),
    Point2D(3, 1),
    Point2D(0, -1),
    Point2D(-2, 1)
]))  # Output: -1

print(solution_version_1([
    Point2D(-1, 3),
    Point2D(1, 2),
    Point2D(1, 1),
    Point2D(3, 1),
    Point2D(0, -1),
    Point2D(-2, 1),
    Point2D(-1, 2)
]))  # Output: 2 or 6 (depending on the sorting order)


# Version 2
# Source
# https://juejin.cn/post/7227098017555529788
# from extratypes import Point2D  # library with types used in the task

def solution_version_2(A):
    result = 0
    is_convex = True

    for p0, p1, p2 in zip(A, A[1:] + A[:1], A[2:] + A[:2]):
        p0p1_x, p0p1_y = p1.x - p0.x, p1.y - p0.y
        p0p2_x, p0p2_y = p2.x - p0.x, p2.y - p0.y
        p0p1_p0p2 = p0p1_x * p0p2_y - p0p1_y * p0p2_x

        if p0p1_p0p2 < 0:
            if result > 0:
                is_convex = False
                break
            result -= 1
        if p0p1_p0p2 > 0:
            if result < 0:
                is_convex = False
                break
            result += 1

    if is_convex:
        return -1

    min_point_i = 0
    min_x, min_y = A[0].x, A[0].y

    for i, a in enumerate(A[1:]):
        if a.y < min_y:
            min_x, min_y = a.x, a.y
            min_point_i = i + 1
        elif a.y == min_y:
            if a.x < min_x:
                min_x = a.x
                min_point_i = i + 1

    is_clockwise = True
    tmp_A = [A[-1]] + A + [A[0]]
    p0, p1, p2 = tmp_A[min_point_i], tmp_A[min_point_i + 1], tmp_A[min_point_i + 2]

    p0p1_x, p0p1_y = p1.x - p0.x, p1.y - p0.y
    p1p2_x, p1p2_y = p2.x - p1.x, p2.y - p1.y
    p0p1_p0p2 = p0p1_x * p1p2_y - p0p1_y * p1p2_x

    if p0p1_p0p2 > 0:
        is_clockwise = False

    for i, (p0, p1, p2) in enumerate(zip(A[-1:] + A[:-1], A, A[1:] + A[:1])):
        p0p1_x, p0p1_y = p1.x - p0.x, p1.y - p0.y
        p1p2_x, p1p2_y = p2.x - p1.x, p2.y - p1.y
        p0p1_p0p2 = p0p1_x * p1p2_y - p0p1_y * p1p2_x

        if is_clockwise and p0p1_p0p2 > 0:
            return i
        if not is_clockwise and p0p1_p0p2 < 0:
            return i

# Test cases
print(solution_version_2([
    Point2D(-1, 3),
    Point2D(1, 2),
    Point2D(3, 1),
    Point2D(0, -1),
    Point2D(-2, 1)
]))  # Output: -1

print(solution_version_2([
    Point2D(-1, 3),
    Point2D(1, 2),
    Point2D(1, 1),
    Point2D(3, 1),
    Point2D(0, -1),
    Point2D(-2, 1),
    Point2D(-1, 2)
]))  # Output: 2 or 6 (depending on the sorting order)

# 1. The function `solution_verion_2(A)` takes a list of `Point2D` objects as input. These represent the points of a polygon.
# 2. The variable `result` is initialized to 0, which will be used to keep track of the orientation of the polygon
# as the algorithm progresses.
# 3. The variable `is_convex` is set to `True`, assuming that the polygon is convex unless proven otherwise.
# 4. The code iterates through each triplet of consecutive points in the polygon (p0, p1, p2) using the `zip` function.
# It calculates the cross product of vectors p0p1 and p0p2 to determine whether the orientation is clockwise or
# counterclockwise. If the cross product is negative, it means the orientation is counterclockwise, and `result`
# is decremented. If it is positive, the orientation is clockwise, and `result` is incremented.
# The loop also checks if there is a change in orientation (`is_convex` becomes `False`) to detect whether
# the polygon is convex.
# 5. After the loop, if `is_convex` is still `True`, it means the polygon is convex, and the function returns -1.
# 6. If the polygon is not convex, the code proceeds to find the minimum point (the leftmost-bottom point)
# of the polygon.
# It iterates through all points in `A` and updates `min_x` and `min_y` whenever it finds a point with lower
# y-coordinate or equal y-coordinate but lower x-coordinate.
# 7. The variable `is_clockwise` is set to `True`, assuming the polygon is oriented clockwise (which means the
# concavity index will be on the left side when traversed clockwise).
# 8. To calculate the concavity index, the code uses the `tmp_A` list, which is `A` with the last point appended at
# the beginning and the first point appended at the end. This is done to handle cases where the minimum point is either the first or the last point in the original list `A`.
# 9. The code retrieves three consecutive points (p0, p1, p2) from `tmp_A` based on the minimum point's index
# (`min_point_i`).
# It calculates the cross product of vectors p0p1 and p1p2 to determine whether the orientation is clockwise or counterclockwise.
# 10. The loop then iterates through each triplet of consecutive points in the original list `A`,
# calculating the cross product as before. If `is_clockwise` is `True` (indicating that the polygon
# is oriented clockwise), it looks for the first occurrence of a positive cross product.
# This indicates a counterclockwise turn, and the index of this point is returned as the concavity index.
# 11. If `is_clockwise` is `False` (indicating that the polygon is oriented counterclockwise),
# it looks for the first occurrence of a negative cross product. This indicates a clockwise turn,
# and the index of this point is returned as the concavity index.
# 12. If no concavity index is found, it means there was an error or the polygon is degenerate (e.g., a straight line),
# and the function does not return anything, effectively returning `None`.
# In summary, the function first determines if the polygon is convex. If it is, it returns -1.
# If not, it finds the minimum point (leftmost-bottom point) of the polygon and determines the polygon's orientation
# (clockwise or counterclockwise). Based on the orientation, it looks for the first concavity index
# (a point where the polygon bends inward) and returns it.
