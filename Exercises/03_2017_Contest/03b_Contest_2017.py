# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, C, D):
    # Implement your solution here
    from collections import Counter

    # Count the number of each color in clean and dirty socks
    clean_counter = Counter(C)
    dirty_counter = Counter(D)

    pairs = 0

    # Step 1: Try to form pairs from clean socks first
    # Iterate over the dictionary of clean socks
    for color, count in list(clean_counter.items()):
        # Calculate the number of pairs and single socks of the current color
        pair_count, odd = divmod(count, 2)
        # Add the number of pairs to the total
        pairs += pair_count
        # If there is no single sock of this color, remove it from the dictionary
        if odd == 0:
            del clean_counter[color]

    # Step 2: Pair clean with dirty socks
    # For each color that is left in the clean socks dictionary
    for color in list(clean_counter.keys()):
        # If there is remaining washing capacity and there is a dirty sock of this color
        if K > 0 and dirty_counter[color] > 0:
            # Add one to the total number of pairs and decrease the washing capacity
            pairs += 1
            K -= 1
            # Decrease the number of dirty socks of this color
            dirty_counter[color] -= 1

    # Step 3: Pair dirty socks
    # For each color in the dirty socks dictionary
    for color, count in dirty_counter.items():
        # Calculate the number of pairs and single socks of this color
        pair_count, odd = divmod(count, 2)
        # Calculate the number of pairs that can be formed within the washing capacity
        possible_pairs = min(pair_count, K // 2)
        # Add the number of possible pairs to the total
        pairs += possible_pairs
        # Decrease the washing capacity accordingly
        K -= possible_pairs * 2

    return pairs

print(solution(2, [1, 2, 1, 1], [1, 4, 3, 2, 4]))
