def maxRev(l):
    # No.2
    calls[l] += 1
    if mm[l] == -1:
        if l == 0:
            mm[l] = 0
        else:
            mxp = 0
            for c in range(1,l+1):
                mxp = max(mxp, p[c] + maxRev(l-c))
                # print("round ", c, mxp) #Check maximum each round
            mm[l] = mxp
    return mm[l]


p = list(map(int,input().split()))
L = len(p)
p = [0]+p #set index 0 equal to 0
# print(p)

# No.1
calls = [0] * (1 + L)

# No.6
mm = [-1] * (L+1)
print(maxRev(L))
print(calls) # Result no.2