def maxRev(l):
    if l == 0:
        return 0
    else:
        mxp = 0
        for c in range(1,l+1):
            mxp = max(mxp, p[c] + maxRev(l-c))
        return mxp 

p = list(map(int,input().split()))
L = len(p)
p = [0]+p
print(p)
print(maxRev(L))
