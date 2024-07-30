M, N = map(int, input().split())

a = [0]*N
print(a) 
# [0, 0]

b = [i for i in range(N)]
print(b) 
# [0, 1]

c = [[0]*N]*M
print(c) 
# [[0, 0], [0, 0]]

c[0][0] = 1
print(c) 
# [[1, 0], [1, 0]] 
# All the sublists in c are actually references to the same list in memory.
# Each sublist is not independent

d = [[0]*N for i in range(M)]
d[0][0] = 1
print(d) 
# [[1, 0], [0, 0]]
# All the sublists in c are not references to the same list in memory.
# Each sublist is independent
