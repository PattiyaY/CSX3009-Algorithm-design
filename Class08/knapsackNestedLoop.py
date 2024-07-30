import sys
sys.setrecursionlimit(10000)

def knapsack(N, M, w, v):
    # Initialize the memoization table with 0s
    mm = [[0] * (M + 1) for _ in range(N + 1)]

    # Fill the table in bottom-up manner
    for i in range(N - 1, -1, -1):
        for C in range(M + 1):
            # If we skip the item i
            skip = mm[i + 1][C]
            
            # If we take the item i (if it fits in the current capacity C)
            take = 0
            if w[i] <= C:
                take = v[i] + mm[i + 1][C - w[i]]
            
            # Choose the maximum of taking or skipping the item
            mm[i][C] = max(skip, take)

    # The result is in mm[0][M]
    return mm[0][M]

# Example usage:
N, M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

print(knapsack(N, M, w, v))
