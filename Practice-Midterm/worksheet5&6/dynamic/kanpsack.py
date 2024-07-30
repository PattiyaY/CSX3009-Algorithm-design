# Read input
N, M = map(int, input().split())  # Number of items, Maximum weight capacity
w = list(map(int, input().split()))  # Weights of the items
v = list(map(int, input().split()))  # Values of the items

# Initialize the DP table with zeros
dp = [[0] * (M + 1) for _ in range(N + 1)]

# Fill the DP table
for i in range(1, N + 1):
    for C in range(M + 1):
        if w[i - 1] <= C:
            # Max value by either including or excluding the current item
            dp[i][C] = max(dp[i - 1][C], dp[i - 1][C - w[i - 1]] + v[i - 1])
        else:
            # If the item can't be included, the value is the same as without it
            dp[i][C] = dp[i - 1][C]

# The answer is the maximum value we can carry in the knapsack
print(dp[N][M])
