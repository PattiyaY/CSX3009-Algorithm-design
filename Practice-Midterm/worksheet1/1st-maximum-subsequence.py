def Sum(numList, i, j):     
    s = 0     
    for k in range(i, j + 1):       
        s += numList[k]     
    return s

maxVal = 0
numbers = list(map(int,input().split()))

for i in range(len(numbers)):
    for j in range(i,len(numbers)):
	    maxVal = max(maxVal, Sum(numbers, i, j))
print(maxVal)
