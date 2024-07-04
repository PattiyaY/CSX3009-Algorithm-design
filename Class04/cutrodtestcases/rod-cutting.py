def maxRev(length):
    if length == 0:
        return 0
    else:
        mxRevenue = 0
        for i in range(1,length+1):
            mxRevenue = max(mxRevenue, price[i] + maxRev(length-i))
        return mxRevenue 

price = list(map(int,input().split()))
length = len(price)
price = [0]+ price
print(price)
print(maxRev(length))
