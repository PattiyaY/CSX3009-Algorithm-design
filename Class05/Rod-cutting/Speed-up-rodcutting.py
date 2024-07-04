import sys
sys.setrecursionlimit(10000)
def maxRev(length):
    if checkList[length] == -1:
        # no.2 Check how many calls
        calls[length] += 1
        if length == 0:
            checkList[length] = 0
        else:
            mxRevenue = 0
            for i in range(1,length+1):
                mxRevenue = max(mxRevenue, price[i] + maxRev(length-i))
            checkList[length] = mxRevenue
    return checkList[length] 

price = list(map(int,input().split()))
length = len(price)
price = [0]+ price

# No.1
calls = [0] * (length + 1)

# No.6
checkList = [-1] * (length + 1)

print("Max Revenue:",maxRev(length))
print("Price:",price)
print("Checked list:",checkList)
print("Total calls:",calls) # Result no.2