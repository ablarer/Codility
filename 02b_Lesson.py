# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # pass
    result = 0
    for number in A:
        result ^= number
        print("Decimal Number", number, ", Binary Number", bin(number), ", Decimal Result", result, ", Binary Result", bin(result))
    return result

print(solution([1,2,3,4,5,6,8,6,5,4,3,2,1]))