def max_profit(prices):
    if not prices:
        return 0

    n = len(prices)
    min_price = float('inf')
    max_profit = 0
    memo = {}

    for i in range(n):
        if i == 0:
            memo[i] = 0
        else:
            min_price = min(min_price, prices[i])
            max_profit = max(memo[i-1], prices[i] - min_price)
            memo[i] = max_profit

    return memo[n-1]

# Reading input
prices = list(map(int, input().split()))

# Calculating and printing the maximum profit
print(max_profit(prices))
