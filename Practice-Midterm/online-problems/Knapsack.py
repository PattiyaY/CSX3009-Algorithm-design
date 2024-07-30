N, W = map(int, input().split())
v = [None] * N
w = [None] * N

for i in range(N):
    v[i], w[i] = map(int, input().split())

#Memoization
mm = [[-1]*(W+1) for i in range(N+1)]

def maxVal(i,C):
    if mm[i][C] == -1:
        if i == N or C == 0:
            mm[i][C] = 0
        else:
            skip = maxVal(i+1, C)  # skip item i
            take = 0
            if w[i] <= C:
                take = v[i] + maxVal(i+1, C-w[i])  # take item i
            mm[i][C] = max(skip,take)
    return mm[i][C]

for i in range(N - 1, -1, -1):
    for C in range(W + 1):
        mm[i][C] = maxVal(i,C)

print(mm[0][W])