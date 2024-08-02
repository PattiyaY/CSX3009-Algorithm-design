import sys
sys.setrecursionlimit(10000)

def comb(i):
    if i == n:
        print(x)
    else:
        for a in [0,1,2]:
            x[i] = a
            comb(i+1)


n = int(input())
x = [0] * n  # -> [0,0,0] 
comb(0)