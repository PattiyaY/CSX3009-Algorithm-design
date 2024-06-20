import sys
sys.setrecursionlimit(10000)

#Combination
# Recursive code
def comb(i):
    if i == n:
        print(x)
    else:
        x[i] = 0
        comb(i+1)
        x[i] = 1
        comb(i+1)

n = int(input())
x = [0] * n  # -> [0,0,0] 
comb(0)