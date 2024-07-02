import sys
sys.setrecursionlimit(10000)

def balanceSplit(listNumber, current, firstSum, secondSum):
    if current == len(listNumber):
        return abs(firstSum - secondSum)
    else:
        groupOne = balanceSplit(listNumber, current + 1, firstSum + listNumber[current], secondSum)
        groupTwo = balanceSplit(listNumber, current + 1, firstSum, secondSum + listNumber[current])
        return min(groupOne, groupTwo)


n = list(map(int,input().split()))
current = 0
firstSum = 0
secondSum = 0
print(balanceSplit(n, current, firstSum, secondSum))