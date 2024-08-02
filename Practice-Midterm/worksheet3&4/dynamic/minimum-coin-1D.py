def mainProgramme():
    coin = list(map(int, input().split()))
    V = int(input())
    
    # DP array to store minimum coins for each value
    dp = [float('inf')] * (V + 1)
    dp[0] = 0  # Base case: 0 coins needed for 0 change

    # Iterative DP solution
    for i in range(1, V + 1): #amount of change
        for each in coin:  #each coin in the list
            if each <= i: #check if coin is less than current change or not
                #storing amount of coin we need to pay
                dp[i] = min(dp[i], dp[i - each] + 1) 

    print("Minimum required coins for change:", -1 if dp[V] == 0 else dp[V])
    # if it's not possible to make the change with the given coins, 
    # we'll return -1.
    print("Coins:", coin)
    print("DP array:", dp)

mainProgramme()
