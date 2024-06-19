# Problem no. 1296
# Website : https://acm.timus.ru/

# def calculateLargestGravity(A):
#     max_current = largest_gravity = 0
#     for i in range(1,len(A)-1):
#         max_current += A[i]
#         print(max_current)
#         if max_current > largest_gravity:
#             largest_gravity = max_current
#     return largest_gravity

def calculateLargestGravity(A):
    max_current = max_global = 0 #initail gravity = 0
    for i in range(1,len(A)): #Start from 1 until last
        max_current = max(A[i],max_current+A[i])
        if max_current > max_global:
            max_global = max_current
    return max_global

import sys
numbers = list(map(int, sys.stdin.read().split()))
print(calculateLargestGravity(numbers))
