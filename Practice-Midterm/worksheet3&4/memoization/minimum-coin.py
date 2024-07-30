import sys
sys.setrecursionlimit(10000)

def mincoin(currentChange):
    if checkList[currentChange] == -1:
        calls[currentChange] += 1

        # Base Case: 0 coins needed for 0 change
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


# Memoization (checkList): This array stores the minimum coins      required for each amount from 0 to V. It avoids redundant calculations by storing results of subproblems.

# Recursive Calls (mincoin): The function recursively calculates the minimum coins required, using the memoized results to speed up the process.

# Call Count (calls): This array tracks how many times the function is called for each amount, providing insight into the recursion depth and efficiency.