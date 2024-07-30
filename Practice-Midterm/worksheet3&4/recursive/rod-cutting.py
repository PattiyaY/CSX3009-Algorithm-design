def mainProgramme():
    rodPrice = list(map(int, input().split()))
    n = len(rodPrice)

    # Recursive solution
    def maxRev(l):
        if l == 0:
           return 0
        maxEarn = float("-inf")
        for i in range(1, l + 1):
            if i <= n:
                tmp = rodPrice[i - 1] + maxRev(l - i)
                if tmp > maxEarn:
                    maxEarn = tmp
        return maxEarn

    print(maxRev(n))
mainProgramme()