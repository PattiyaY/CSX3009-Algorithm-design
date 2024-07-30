# Read input
firstWord = input()
secondWord = input()

firstLength = len(firstWord)
secondLength = len(secondWord)

# Initialize memoization table with None to indicate uncomputed states
memo = [[None] * (secondLength + 1) for _ in range(firstLength + 1)]

def editDistance(i, j):
    # Base cases
    if i == firstLength and j < secondLength:
        return secondLength - j
    if i < firstLength and j == secondLength:
        return firstLength - i
    if i == firstLength and j == secondLength:
        return 0

    # Check if the result for this state has already been computed
    if memo[i][j] is not None:
        return memo[i][j]

    # If characters match, no operation is needed
    if firstWord[i] == secondWord[j]:
        memo[i][j] = editDistance(i + 1, j + 1)
    else:
        # Consider all three operations: insert, delete, change
        insert = 1 + editDistance(i, j + 1)
        delete = 1 + editDistance(i + 1, j)
        change = 1 + editDistance(i + 1, j + 1)
        memo[i][j] = min(insert, delete, change)

    return memo[i][j]

# Compute and print the result
print(editDistance(0, 0))
