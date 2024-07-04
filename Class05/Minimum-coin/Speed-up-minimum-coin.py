import sys
sys.setrecursionlimit(10000)

def mincoin(currentChange):
    if checkList[currentChange] == -1:
        calls[currentChange] += 1
        if currentChange == 0:
            checkList[currentChange] = 0
        else:
            minC = currentChange
            for each in coin:
                if each <= currentChange:
                    minC = min(minC, 1 + mincoin(currentChange-each))
            checkList[currentChange] = minC
    return checkList[currentChange]


coin = list(map(int,input().split()))
V = int(input()) #Current change

length = V + 1
calls = [0] * length
checkList = [-1] * length

print("Minimun required coin for change",mincoin(V))
print("Coin:",coin)
print("Checked list:",checkList)
print("Total calls:",sum(calls), calls) # Result no.2
