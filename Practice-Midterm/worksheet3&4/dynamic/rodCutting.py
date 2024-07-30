def mainProgramme():
    price = list(map(int, input().split()))
    n = len(price)
    
    # DP array to store maximum revenue for each length
    dp = [0] * (n + 1)

    # Iterative DP solution
    for length in range(1, n + 1):
        max_value = float('-inf')
        for i in range(1, length + 1):
            max_value = max(max_value, price[i - 1] + dp[length - i])
        dp[length] = max_value

    print("Maximum Revenue:", dp[n])
    print("Prices:", price)
    print("DP array:", dp)

mainProgramme()
