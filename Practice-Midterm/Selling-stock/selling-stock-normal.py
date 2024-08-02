#Normal approach
def sellingStock(prices):
    if not prices:
        return 0

    minPrice = float("inf")
    maxProfit = 0

    for price in prices:
        if price < minPrice:
            minPrice = price
        elif price - minPrice > maxProfit:
            maxProfit = price - minPrice
            
    return maxProfit

prices = list(map(int, input().split()))
print(sellingStock(prices))