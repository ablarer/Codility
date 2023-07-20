# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# The solution function takes a binary tree represented as a Tree object.
def solution(T):
    maxStep = [0]  # Store the maximum step as a mutable list

    # The dfs function performs a depth-first search traversal of the binary tree
    # and updates the maximum step value.
    def dfs(root, isLeft, step):
        if root is None:
            return
        maxStep[0] = max(maxStep[0], step)  # Update max step so far
        if isLeft:
            dfs(root.l, False, step + 1)  # Keep going from root to left
            dfs(root.r, True, step)  # Restart going from root to right
        else:
            dfs(root.r, True, step + 1)  # Keep going from root to right
            dfs(root.l, False, step)  # Restart going from root to left

    # Start the depth-first search traversal from the root node,
    # considering both left and right directions.
    dfs(T, True, 0)
    dfs(T, False, 0)

    # If the maximum step is 0, it means there is no zigzag path.
    # In that case, return 0. Otherwise, return the maximum step - 1.
    if maxStep[0] == 0:
        return 0
    return maxStep[0] - 1

# The code uses a recursive depth-first search (DFS) approach to traverse the binary tree and find the longest
# zigzag path.
# The dfs function is called twice, once considering the left direction (isLeft=True) and once considering
# the right direction (isLeft=False).
# During the DFS traversal, the maxStep variable is updated to keep track of the maximum step encountered so far.
# The maxStep variable is stored as a mutable list to allow modifications within the nested dfs function.
# Finally, the function returns the length of the longest zigzag path by subtracting 1 from the maximum step value.
# If there is no zigzag path (maximum step is 0), the function returns 0.