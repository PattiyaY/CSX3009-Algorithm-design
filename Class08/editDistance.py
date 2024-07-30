def editDistance(word1, word2):
    lenOne = len(word1)
    lenTwo = len(word2)

    # 2 dimensional array
    cache = [[float('inf')] * (lenTwo + 1) for i in range(lenOne + 1)]
    # print(cache)

    for j in range(lenTwo + 1):
        cache[lenOne][j] = lenTwo - j
    for i in range(lenOne+ 1):
        cache[i][lenTwo] = lenOne - i

    for i in range(lenOne - 1, -1, -1):
        for j in range(lenTwo -1, -1, -1):
            if word1[i] == word2[j]:
                # print(word1[i], word2[j])
                cache[i][j] = cache[i+1][j+1]
            else:
                # find min of insert, delete, replace
                cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])
            print(cache)
    return cache[0][0]

print(editDistance("Hi", "Hello"))