def mainProgramme():
    coin = list(map(int, input().split()))
    V = int(input())
    
    # DP array to store minimum coins for each value
    dp = [float('inf')] * (V + 1)
    dp[0] = 0  # Base case: 0 coins needed for 0 change

    # Iterative DP solution
    for i in range(1, V + 1):
        for each in coin:
            if each <= i:
                dp[i] = min(dp[i], dp[i - each] + 1)

    print("Minimum required coins for change:", dp[V])
    # if it's not possible to make the change with the given coins, 
    # we'll return -1.
    print("Coins:", coin)
    print("DP array:", dp)

mainProgramme()
