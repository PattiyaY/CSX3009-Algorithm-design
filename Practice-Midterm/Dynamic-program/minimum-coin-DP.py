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


def min_coins(coins, V):
    # Create a list to store the minimum number of coins needed for each value
    length = V + 1
    checkList = [float('inf')] * length
    checkList[0] = 0  # Base case: 0 coins are needed to make amount 0

    for i in range(1, length):
        for coin in coins:
            if i >= coin:
                checkList[i] = min(checkList[i], checkList[i - coin] + 1)

    return checkList[V] if checkList[V] != float('inf') else -1

coins = [1, 4, 5]
V = len(coins)

print(min_coins(coins, 13))  # Output: 3
print(min_coins(coins, 150)) # Output: 30