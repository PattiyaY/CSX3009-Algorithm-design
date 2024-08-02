# Modify from a2, count k 1's 
# Eg. k = 3, how many 1's that is in X 3 times 
# k = 3 and there's [1,1,1] -> 1 time
# So it should return 1.
import sys
sys.setrecursionlimit(10000)

def comb(i):
    if i == n:
        if sum(x) == k:
            return 1
        else:
            return 0
    else:
        x[i] = 0
        s = comb(i+1)
        x[i] = 1
        s += comb(i+1)
        return s
    
n = int(input())
k = int(input())
x = [0] * n  # -> [0,0,0] 

print(comb(0))