def grid_paths(n, m):
    # Use a 2D list to store the number of paths
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Base case: Start at (1, 1)
    dp[1][1] = 1
    
    # Initialize the first row and first column
    for i in range(1, n + 1):
        dp[i][1] = 1
    for j in range(1, m + 1):
        dp[1][j] = 1

    # Fill in the rest of the grid
    for i in range(2, n + 1):
        for j in range(2, m + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    # Return the number of paths to the bottom-right corner
    return dp[n][m]

# Example usage
print(grid_paths(3, 3))  # Output: 6
print(grid_paths(7, 3))  # Output: 28
print(grid_paths(18, 6))  # Output: 26334
