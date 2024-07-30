import sys
sys.setrecursionlimit(10000)

def maxVal(i, C):
    if i == N:
        return 0
    if memo[i][C] != -1:
        return memo[i][C]

    # Option 1: Skip the current item
    skip = maxVal(i + 1, C)
    
    # Option 2: Take the current item, if it fits in the remaining capacity
    if w[i] <= C:
        take = v[i] + maxVal(i + 1, C - w[i])
    else:
        take = -1

    memo[i][C] = max(skip, take)
    return memo[i][C]

N, M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

# Initialize the memoization table with -1 (indicating that no result has been computed yet)
memo = [[-1] * (M + 1) for _ in range(N)]

print(maxVal(0, M))
