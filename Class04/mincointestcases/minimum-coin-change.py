def mincoin(v):
    if v == 0:
        return 0
    else:
        mc = v
        for c in coins:
            if c <= v:
                mc = min(mc,1 + mincoin(v-c))
        return mc



coins = list(map(int,input().split()))
v = int(input())
print(mincoin(v))
# print(coin,v)

# coin = [5, 4, 3, 1]
# i = 0
# X = 7
# def minCoin(i,X,coin):
#     answer = 0
#     sum = 0
#     while(sum != X):
#         if (sum + coin[i] < X):
#             sum = sum + coin[i]
#             answer += 1
#         elif coin[i] > sum:
#             i+=1
#         else:
#             break
#     return answer
        
# print(minCoin(i,X,coin))