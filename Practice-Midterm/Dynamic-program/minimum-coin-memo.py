#Memoization
memo = {} #added this line

def minimum_coins(m, coins):
    if m in memo: #added this line
        return memo[m] #added this line
    
    if m == 0:
        return 0
    else:
        answer = float("inf")
        for coin in coins:
            subproblem = m - coin 
            if subproblem < 0:
                continue
            answer = min(answer, 1 + minimum_coins(subproblem, coins))
    memo[m] = answer #added this line
    return answer

print(minimum_coins(13, [1,4,5]))
print(minimum_coins(150, [1,4,5]))

#Time complexity is O(m*k) m -> target sum, k -> number of coins

