#2nd Approach 
def Sum(x, i, j):
    s= x[j]
    if i > 0:
        s -= x[i-1]
    return s

import time

start = time.process_time()
numbers = list(map(int, input().split()))
n = len(numbers)
for i in range(1,n):
    numbers[i] += numbers[i-1] #Accumulated list

maxS = 0
for i in range(n):
    for j in range(i,n):
        s = Sum(numbers, i, j)
        maxS = max(s,maxS)
print(maxS)


finish = time.process_time()
print("running time =", finish-start)