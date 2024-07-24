testCase = int(input())
ans = []

for _ in range(testCase):
    n, k = list(map(int, input().split()))
    price = list(map(int, input().split()))
    ans.append(price[k-1])

for num in ans:
    print(num)

