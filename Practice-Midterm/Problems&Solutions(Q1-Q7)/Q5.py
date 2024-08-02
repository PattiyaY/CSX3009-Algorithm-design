def max_money_from_rice():
    # Read the total weight of the rice
    W = int(input())
    # Read the number of possible sack sizes
    k = int(input())
    
    # Initialize the list to store sack sizes and prices
    sacks = []
    for _ in range(k):
        size, price = map(int, input().split())
        sacks.append((size, price))
    
    # Initialize the DP table with zeros
    dp = [0] * (W + 1)
    
    # Fill the DP table
    for size, price in sacks:
        for weight in range(size, W + 1):
            #subtract total weight from current size and add price
            dp[weight] = max(dp[weight], dp[weight - size] + price)
    
    # The answer is the maximum money for W kilograms of rice
    print(dp[W])

# Call the function to execute
max_money_from_rice()
