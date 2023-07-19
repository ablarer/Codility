# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, M):
    # Implement your solution here
    # pass

    def gcd(a, b):
        if b == 0:
            return a

        return gcd(b, a % b)

    # Find the greatest common divisor
    gcd_value = gcd(N, M)

    # Calculate the number of chocolates
    number_of_chocolates = N // gcd_value

    return number_of_chocolates

print(solution((10, 4)))