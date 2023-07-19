# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # pass
    if len(A) < 2:
        return 0

    min_price = A[0]
    max_profit = 0

    for price in A:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

print(solution([23171, 21011, 21123, 21366, 21013, 21367]))