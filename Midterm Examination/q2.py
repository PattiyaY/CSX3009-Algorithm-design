def min_cost_to_reach_last_stone(S):
    n = len(S)
    # Initialize dp array with infinity for all except the first
    dp = [float('inf')] * n
    dp[0] = 0
    
    # Fill the dp array
    for i in range(1, n):
        # value to jump from i-1 to i
        dp[i] = min(dp[i], dp[i-1] + abs(S[i] - S[i-1]))
        
        if i > 1:
            #  value to jump from i-2 to i
            dp[i] = min(dp[i], dp[i-2] + abs(S[i] - S[i-2]))
    
    # The answer is the minimum possible value of connected subsequence
    return dp[-1]

# Input reading
S = list(map(int, input().split()))

# Calculate and print the minimum cost
print(min_cost_to_reach_last_stone(S))
