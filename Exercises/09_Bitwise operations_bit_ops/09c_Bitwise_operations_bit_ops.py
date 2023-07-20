# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here

    # 0x55555555 has an alternating pattern of 1s and 0s in its binary representation:
    # 0101 0101 0101 0101 0101 0101 0101 0101.

    # 0xAAAAAAAA has all its bits set to 1 in positions where N's binary representation has consecutive 1s:
    # 1010 1010 1010 1010 1010 1010 1010 1010.

    # By performing a bitwise AND operations:
    # a will contain the bits of N that are in positions where there are no consecutive 1s,
    # Bits of N are preserved only where the 0x55555555 has corresponding 1s.
    # This effectively removes the consecutive 1s from N.

    # b will contain the bits of N that are in positions where there are consecutive 1s.
    # Bits of N are preserved only where the 0xAAAAAAAA has corresponding 1s.
    # This isolates the consecutive 1s in N.

    a = N & 0x55555555
    b = N & 0xAAAAAAAA

    print(f"0x55555555: {bin(0x55555555)}")
    print(f"0xAAAAAAAA: {bin(0xAAAAAAAA)}")
    print(f"N: {bin(N)}\t{N}")
    print(f"a = N & 0x55555555 = {bin(a)}\t{a}")
    print(f"b = N & 0xAAAAAAAA = {bin(b)}\t\t{b}")

    # The code checks if the sum of a and b equals N. If the sum is equal, it means that a and b form a sparse decomposition of N.
    #
    #     If (a + b == N), it implies that the non-consecutive 1s from a and the consecutive 1s from b add up to N.
    #     In this case, a is returned as one part of the sparse decomposition.
    #
    # If the sum of a and b does not equal N, it means that a sparse decomposition of N does not exist, and the code returns -1.

    if (a + b == N):
        return a, b

    return -1

print(solution(26))
print(solution(25))
print(solution(24))
print(solution(7))
print(solution(3))