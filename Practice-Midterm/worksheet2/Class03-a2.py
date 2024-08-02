# Counting number of Combinations
import sys
sys.setrecursionlimit(10000)

# Recursive code
def comb(i):
    if i == n:
        print(x)
        return 1
    else:
        x[i] = 0
        s = comb(i+1)
        x[i] = 1
        s += comb(i+1)
        return s


n = int(input())
x = [0] * n  # -> [0,0,0] 
print(comb(0))


