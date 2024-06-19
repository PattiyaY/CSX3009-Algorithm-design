#3rd Approach 
def kadane(A):
    max_current = max_global = A[0]
    for i in range(1,len(A)-1): #start from 1 until end of list
        max_current = max(A[i],max_current+A[i])
        if max_current > max_global:
            max_global = max_current
    return max_global

import time

start = time.process_time()
numbers = list(map(int, input().split()))

print(kadane(numbers))

finish = time.process_time()
print("running time =", finish-start)