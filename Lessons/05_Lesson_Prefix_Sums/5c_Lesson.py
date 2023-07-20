def solution_version_1(S, P, Q):
        impact_factors = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
        sequence = [impact_factors[nucleotide] for nucleotide in S]

        result = []

        for i in range(len(P)):
            start = P[i]
            end = Q[i]

            min_impact_factor = min(sequence[start:end + 1])

            result.append(min_impact_factor)

        return result

print(solution_version_1('CAGCCTA', [2, 5, 0], [4, 5, 6]))


def solution_version_2(S, P, Q):
    # Preprocess the DNA sequence
    nucleotides = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    sequence = [[0] * (len(S) + 1) for _ in range(4)]

    for i in range(len(S)):
        nucleotide = nucleotides[S[i]]
        for j in range(4):
            sequence[j][i + 1] = sequence[j][i] + (j == nucleotide)

    # Process each query
    result = []
    for i in range(len(P)):
        start = P[i]
        end = Q[i]

        # Find the minimum impact factor within the given range
        for j in range(4):
            if sequence[j][end + 1] - sequence[j][start] > 0:
                result.append(j + 1)
                break

    return result

print(solution_version_2('CAGCCTA', [2, 5, 0], [4, 5, 6]))
