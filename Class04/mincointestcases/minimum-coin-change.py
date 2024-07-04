import sys
sys.setrecursionlimit(10000)

def mincoin(currentChange):
    if currentChange == 0:
        return 0
    else:
        minC = currentChange
        for each in coin:
            if each <= currentChange:
                minC = min(minC, 1 + mincoin(currentChange-each))
        return minC



coin = list(map(int,input().split()))
coin = [0] + coin #set index 0 equal to 0

V = int(input()) #Current change
print(mincoin(V))