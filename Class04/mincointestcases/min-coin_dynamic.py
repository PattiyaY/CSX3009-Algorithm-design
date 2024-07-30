def mincoin(coin, V):
    for i in range(1, V + 1):
        for c in coin:
            if c <= i:
                dp[i] = min(dp[i], dp[i - c] + 1)

    return dp[V] if dp[V] != float('inf') else -1  
    # Return -1 if no solution exists


# Input coins and amount
coin = list(map(int, input().split()))
V = int(input())

# Initialize the dp array to store the minimum coins required for each amount
dp = [float('inf')] * (V + 1)
dp[0] = 0  # Base case: no coins needed to make 0 change

print(mincoin(coin, V))