import sys
sys.setrecursionlimit(10000)

def maxVal(i,C):
    global count
    count += 1
    if i == N:
        return 0
    else:
        skip = maxVal(i+1,C)
        if w[i] <= C:
            take = v[i] + maxVal(i+1, C-w[i])
            print(take)
        else:
            take = -1
        return max(skip, take)

N,M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))
count = 0
# print(N,M,w,v)
print(maxVal(0,M))