# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # pass
    count = 0
    east_cars = 0

    for car in A:
        if car == 0:
            east_cars += 1
            print("East Car:", car)
            print("Number of east cars:", east_cars, "\n")
        else:
            count += east_cars
            print("West Car:", car)
            print("Count:", count, "\n")

    return count if count <= 1_000_000_000 else -1

print("\nSolution", solution([0, 1, 0, 1, 1]))