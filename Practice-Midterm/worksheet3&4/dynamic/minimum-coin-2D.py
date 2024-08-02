coins = [1,2,4]
V = 3

def minicoin():
    dp = [[float("inf")] * (V+1) for _ in range((len(coins)+1))]

    for i in range(len(dp)):
        dp[i][0] = 0
    
    for j in range(len(dp)):
        dp[0][j] = 0

    for i in range(1,len(dp)): #coins
        for j in range(1,len(dp[0])): # amount of change
            if coins[i-1] <= j: #check if coin is less than amount of change
                #storing amount of coin we need to pay
                dp[i][j] = min(dp[i][j], 1 + dp[i][j - coins[i-1]]) 
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[V][V])

            



    # print(dp)

minicoin()