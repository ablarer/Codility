# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # pass
    N = len(A)
    peaks = []
    for i in range(1, N - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks.append(i)

    num_peaks = len(peaks)

    if num_peaks < 2:
        return num_peaks

    start = 1
    end = num_peaks
    max_flags = 0

    while start <= end:
        k = (start + end) // 2
        flags_placed = 1
        prev_flag_idx = peaks[0]

        for i in range(1, num_peaks):
            if peaks[i] - prev_flag_idx >= k:
                flags_placed += 1
                prev_flag_idx = peaks[i]

        if flags_placed >= k:
            max_flags = k
            start = k + 1
        else:
            end = k - 1

    return max_flags

print(solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))