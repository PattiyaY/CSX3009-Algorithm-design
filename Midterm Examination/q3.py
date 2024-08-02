import time

def f(i,A):
    if checkList[i] == -1:
    
        if i == n or A > half:
            checkList[i] = 0
    
    else:
        iB = x[i] + f(i+1, A)
        iA = 1000000000
        if A+x[i] <= half:
            iA = -x[i] + f(i+1, A+x[i])
        checkList[i] = min(iA,iB)
    return 0 if checkList[i] == -1 else checkList[i]

start = time.process_time()
n = int(input())
x = list(map(int, input().split()))
half = sum(x)//2

checkList = [-1] * n
print(f(0,0))
finish = time.process_time()
print("running time =", finish-start)
