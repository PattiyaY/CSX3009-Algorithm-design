def min_cost_to_reach_last_stone(n, heights):
    # Initialize dp array with infinity for all except the first stone
    dp = [float('inf')] * n
    dp[0] = 0
    
    # Fill the dp array
    for i in range(1, n):
        # Cost to jump from stone i-1 to i
        dp[i] = min(dp[i], dp[i-1] + abs(heights[i] - heights[i-1]))
        
        if i > 1:
            # Cost to jump from stone i-2 to i
            dp[i] = min(dp[i], dp[i-2] + abs(heights[i] - heights[i-2]))
    
    # The answer is the cost to reach the last stone
    return dp[-1]

# Input reading
n = int(input())
heights = list(map(int, input().split()))

# Calculate and print the minimum cost
print(min_cost_to_reach_last_stone(n, heights))
