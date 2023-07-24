# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(A, X):
    # Implement your solution here
    # Initialize a dictionary to store the counts of each fence length
    fence_count = {}
    for fence in A:
        fence_count[fence] = fence_count.get(fence, 0) + 1

    # Initialize the answer and the list of candidate fences
    answer = 0
    candidate_fences = []

    # For each fence length
    for fence, count in fence_count.items():
        # If there are more than one of this fence
        if count > 1:
            # Add it to the list of candidate fences
            candidate_fences.append(fence)
        # If there are more than three of this fence and a square pen of this size meets the area requirement
        if count > 3 and fence * fence >= X:
            # Increase the answer by one
            answer += 1

    # Sort the candidate fences
    candidate_fences.sort()

    # For each pair of candidate fences
    for i in range(len(candidate_fences)):
        for j in range(i + 1, len(candidate_fences)):
            # If a pen with these fence lengths meets the area requirement
            if candidate_fences[i] * candidate_fences[j] >= X:
                # Increase the answer by one
                answer += 1

    # If the answer is greater than 1,000,000,000
    if answer > 1000000000:
        # Return -1
        return -1

    # Return the answer
    return answer
