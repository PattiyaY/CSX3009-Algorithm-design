firstWord = input()
secondWord = input()

firstLength = len(firstWord)
secondLength = len(secondWord)

def editDistance(i,j):
    if i == firstLength and j < secondLength:
        return secondLength - j
    if i < firstLength and j == secondLength:
        return firstLength - i
    if i == firstLength and j == secondLength:
        return 0
    else:
        if firstWord[i] == secondWord[j]:
            return editDistance(i+1, j+1)
        else:
             insert = 1 + editDistance(i, j+1)
             delete = 1 + editDistance(i+1, j)
             change = 1 + editDistance(i+1, j+1)
             return min(insert,delete,change)
        
print(editDistance(0,0))