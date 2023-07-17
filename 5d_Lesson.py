def solution(A):
    N = len(A)
    min_average = float('inf')
    min_start_position = 0

    for start in range(N - 1):
        # Calculate the average of the slice of length 2
        average2 = (A[start] + A[start + 1]) / 2
        if average2 < min_average:
            min_average = average2
            min_start_position = start

        if start < N - 2:
            # Calculate the average of the slice of length 3
            average3 = (A[start] + A[start + 1] + A[start + 2]) / 3
            if average3 < min_average:
                min_average = average3
                min_start_position = start

    return min_start_position

print(solution([4, 2, 2, 5, 1, 5, 8]))
