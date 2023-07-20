# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C):
    # Implement your solution here
    # counts the number of possibilities based on the binary representations of the input integers A, B, and C,
    # considering the position-wise conformity using bitwise operations.
    # n stand for the number of counted occurences

    nA = 0
    nB = 0
    nC = 0

    nAorB = 0
    nAorC = 0
    nBorC = 0
    nAorBorC = 0

    AorB = A | B
    AorC = A | C
    BorC = B | C
    AorBorC = A | B | C

    # For each bit position i, the code checks if the corresponding bit in A, B, and C is 0 using bitwise
    # operations and bitwise AND (&).
    # If the bit at position i in A is 0, nA is incremented.
    # If the bit at position i in B is 0, nB is incremented.
    # If the bit at position i in C is 0, nC is incremented.
    # The same process is followed for the combinations AorB, AorC, BorC, and AorBorC.

    for i in range(30):
        if ((A >> i) & 0x01) == 0:
            nA += 1
        if ((B >> i) & 0x01) == 0:
            nB += 1
        if ((C >> i) & 0x01) == 0:
            nC += 1

        if ((AorB >> i) & 0x01) == 0:
            nAorB += 1
        if ((AorC >> i) & 0x01) == 0:
            nAorC += 1
        if ((BorC >> i) & 0x01) == 0:
            nBorC += 1

        if ((AorBorC >> i) & 0x01) == 0:
            nAorBorC += 1

    print("A:\t\t\t\t", bin(A))
    print("B:\t\t\t\t", bin(B))
    print("C:\t\t\t\t", bin(C))
    print("A or B:\t\t\t", bin(AorB))
    print("A or C:\t\t\t", bin(AorC))
    print("B or C:\t\t\t", bin(BorC))
    print("A or B or C:\t", bin(AorBorC))
    print("nA", nA)
    print("nB", nB)
    print("nC", nC)
    print("nAorB", nAorB)
    print("nAorC", nAorC)
    print("nBorC", nBorC)
    print("nAorBorC", nAorBorC)

    print("AorB", AorB)
    print("AorC", AorC)
    print("BorC", BorC)
    print("AorBorC", AorBorC)

    # The total number of possibilities considering the set bits in A, B, and C individually.
    # The result is obtained by adding the numbers of possibilities for A, B, and C
    # -> 1 shifted left by the corresponding counts: 1 << nA, 1 << nB, 1 << nC


    # Eliminating the duplicates that might arise when counting the possibilities for A, B, and C individually.
    # Subtracting the numbers of possibilities for A or B, A or C, and B or C
    # -> 1 shifted left by the corresponding counts: 1 << nAorB, 1 << nAorC, 1 << nBorC

    # Account for the distinct possibilities that arise when considering A, B, and C together.
    # Adding the number of possibilities for A or B or C
    # -> 1 shifted left by nAorBorC: 1 << nAorBorC

    print(f"1 << nA: {1 << nA}\n1 << nB: {1 << nB}\n1 << nC: {1 << nC}\n1 << nAorB: {1 << nAorB}\n1 << nAorC: {1 << nAorC}\n1 << nBorC: {1 << nBorC}\n1 << nAorBorC: {1 << nAorBorC}")

    result = (1 << nA) - (1 << nAorB) - (1 << nAorC) - (1 << nBorC) + (1 << nB) + (1 << nC) + (1 << nAorBorC)

    return result

print(solution(1073741727, 1073741631, 1073741679))
