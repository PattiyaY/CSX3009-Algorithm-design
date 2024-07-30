# without memo will get the result very slow
def minimum_coins(m, coins):
    if m == 0:
        return 0
    else:
        answer = float("inf")
        for coin in coins:
            subproblem = m - coin 
            if subproblem < 0:
                continue
            answer = min(answer, 1 + minimum_coins(subproblem, coins))
    return answer

print(minimum_coins(13, [1,4,5]))
print(minimum_coins(150, [1,4,5]))          