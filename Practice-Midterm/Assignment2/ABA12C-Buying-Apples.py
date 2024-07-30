def buyingApple(k, prices):
    #base case buy 0 kg return 0
    dp = [float('inf')] * (k + 1)
    dp[0] = 0

    #set weight 0 kg at index 0, so we need to start from 1 to k+1
    for weight in range(1, k + 1):
        #loop through each each possible packet
        for packet_weight in range(1, k + 1):
            #consider packet weight that less than weight we are targeting
            packet_available = prices[packet_weight - 1]
            if packet_weight <= weight and packet_available != -1:
                dp[weight] = min(dp[weight], dp[weight - packet_weight] + packet_available)

    return dp[k] if dp[k] != float('inf') else -1


#number of test cases
c = int(input())

for _ in range(c):
    #number of friends, amount of apple in kilo that he has to buy
    N, K = map(int, input().split())

    #price sequences from 1 to k kilo
    prices = list(map(int, input().split()))

    print(buyingApple(K, prices))

# INPUT:
# 3 5
# -1 -1 4 5 -1
# OUTPUT: -1
