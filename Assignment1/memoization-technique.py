def compute(num):
    if num in cache:
        return cache[num]
    
    result = num*num
    cache[num] = result
    return result

cache = {}
n = int(input())
print(compute(n))
print(cache)