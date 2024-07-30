# Read input
firstWord = input()
secondWord = input()

firstLength = len(firstWord)
secondLength = len(secondWord)

# Initialize the DP table
dp = [[0] * (secondLength + 1) for _ in range(firstLength + 1)]

# Fill the base cases
for i in range(firstLength + 1):
    dp[i][0] = i  # Deleting all characters from firstWord

for j in range(secondLength + 1):
    dp[0][j] = j  # Inserting all characters of secondWord

# Fill the DP table
for i in range(1, firstLength + 1):
    for j in range(1, secondLength + 1):
        if firstWord[i - 1] == secondWord[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]  # Characters match, no operation needed
        else:
            insert = 1 + dp[i][j - 1]
            delete = 1 + dp[i - 1][j]
            change = 1 + dp[i - 1][j - 1]
            dp[i][j] = min(insert, delete, change)

# The answer is the edit distance for the entire strings
print(dp[firstLength][secondLength])
