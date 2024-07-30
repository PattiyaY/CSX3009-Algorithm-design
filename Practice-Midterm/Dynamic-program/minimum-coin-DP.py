def minimum_coins(m, coins):
    # Use a list to store the minimum number of coins needed for each amount
    dp = [float("inf")] * (m + 1)
    dp[0] = 0 # base case

    for i in range(1, m + 1):  # change from recursive to loop instead
        dp[i] = float("inf")
        for coin in coins:
            subproblem = i - coin
            # i - coin is
            # track and solve the problem 
            # for the remaining amount after using one coin
            if subproblem < 0:
                continue
            
            dp[i] = min(dp[i], 1 + dp[subproblem])

    return dp[m] if dp[m] != float("inf") else -1

print(minimum_coins(13, [1, 4, 5]))  # Output: 3
print(minimum_coins(150, [1, 4, 5])) # Output: 30
