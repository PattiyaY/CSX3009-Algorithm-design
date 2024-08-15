#Memoization
import sys
sys.setrecursionlimit(10001)

FLAT = 0
UPPER2 = 1
LOWER2 = 2

L = int(input())
memo = [-1] * (L+1)

def nWays(d, s):
    if memo[d] == -1:
        if d == L:
            if s == FLAT:
                memo[d] = 1  # Assign 1 to memo[d] directly
            else:
                memo[d] = 0  # Assign 0 to memo[d] directly
        else:
            counter = 0
            if s == FLAT:
                counter += nWays(d+1, UPPER2)
                counter += nWays(d+1, LOWER2)   # Symmetric to UPPER2 
                if d < L-1:
                    counter += nWays(d+2, FLAT)
            else:  # s is either UPPER2 or LOWER2
                counter += nWays(d+1, FLAT)
                if d < L-1:
                    counter += nWays(d+2, s)
        
            memo[d] = counter  # Store the result in memo[d]
    return memo[d]

# Start from 0 until L
print(nWays(0, FLAT))



