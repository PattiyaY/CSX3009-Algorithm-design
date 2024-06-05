import sys
import math
numbers = list(map(int, sys.stdin.read().split()))
result = reversed(list(map(math.sqrt, numbers)))
# print(numbers)
for num in result:
    print(round(num,4))