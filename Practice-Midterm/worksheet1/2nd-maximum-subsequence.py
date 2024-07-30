def Sum(numList, i, j):     
    s = numList[j] 
    if i > 0:
        s -= numList[i-1]
    return s

maxVal = 0
numbers = list(map(int,input().split()))
n = len(numbers)

#Accumulated list
for i in range(1,n):
    numbers[i] += numbers[i-1]

for i in range(n):
    for j in range(i,n):
	    maxVal = max(maxVal, Sum(numbers, i, j))
print(maxVal)
