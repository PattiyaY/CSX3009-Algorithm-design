import time

start = time.process_time()

# 1st Approach
def Sum(x, i, j):
    s = 0
    for k in range(i, j+1):
        s += x[k]
    return s
numbers = list(map(int, input().split()))
maxS = 0
n = len(numbers)
for i in range(n):
    for j in range(i,n):
        s = Sum(numbers, i, j)
        maxS = max(s,maxS)
print(maxS)

finish = time.process_time()
print("running time =", finish-start)
