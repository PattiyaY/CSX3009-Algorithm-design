def mainProgramme():
    tiles = list(map(int, input().split()))
    L = int(input())
    
    # DP array to store minimum tiles for each value
    dp = [float('inf')] * (L + 1)
    dp[0] = 0  # Base case: 0 tile needed for 0 coverage

    # Iterative DP solution
    for i in range(1, L + 1): #amount of tiles
        for each in tiles:  #each tile in the list
            if each <= i: #check if tiles is less than current amount of tiles or not
                #storing amount of tiles we need to cover
                dp[i] = min(dp[i], dp[i - each] + 1) 

    print("Minimum required tiles for cover:", -1 if dp[L] == 0 else dp[L])
    # if it's not possible to make the coverage with the given tiles, 
    # we'll return -1.
    print("tiles:", tiles)
    print("DP array:", dp)

mainProgramme()