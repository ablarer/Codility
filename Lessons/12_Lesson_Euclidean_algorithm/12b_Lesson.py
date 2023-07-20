# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # Implement your solution here
    # pass
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def has_same_prime_divisors(a, b):
        gcd_value = gcd(a, b)

        while a != 1:
            a_gcd = gcd(a, gcd_value)
            if a_gcd == 1:
                break
            a //= a_gcd

        if a != 1:
            return False

        while b != 1:
            b_gcd = gcd(b, gcd_value)
            if b_gcd == 1:
                break
            b //= b_gcd

        return b == 1

    count = 0

    for i in range(len(A)):
        if has_same_prime_divisors(A[i], B[i]):
            count += 1

    return count


print(solution([15, 10, 9], [75, 30, 5]))