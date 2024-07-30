def longest_common_subsequence(A, B):
    n = len(A)
    m = len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            #in case A[i-1] == B[j-1] 
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]

# Input
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(longest_common_subsequence(A, B))
