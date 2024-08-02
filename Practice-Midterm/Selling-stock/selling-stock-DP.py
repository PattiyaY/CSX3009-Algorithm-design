def max_profit(prices):
    if not prices:
        return 0

    n = len(prices)
    dp = [0] * n
    min_price = prices[0]

    for i in range(1, n): #loop from 1 to n
         #find the smallest value between 2 numbers Eg. prices[0] vs prices[1] and so on.
        min_price = min(min_price, prices[i])
        #find max value by comparing between previous result and current result
        dp[i] = max(dp[i-1], prices[i] - min_price) 
    
    return dp[-1]

# Reading input
prices = list(map(int, input().split()))

# Calculating and printing the maximum profit
print(max_profit(prices))
