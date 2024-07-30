import sys
sys.setrecursionlimit(10000)

def helper():
    coins = list(map(int,input().split()))
    V = int(input())

    def mincoin(v):
        if v == 0:
            return 0
        if v in coins:
            return 1
        else:
            # set initial value
            min_coin = float("inf")
            # loop each coin
            for each in coins:
                # check if a coin value is less than current v
                if each <= v:
                    # find the minimum coin
                    min_coin = min(min_coin, 1 + mincoin(v-each))

            return min_coin

    print(mincoin(V))
helper()