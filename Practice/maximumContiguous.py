def Sum(x, i, j):
    s = 0
    for k in range(i, j+1):
        if maxVal < (s + x[k]):

            s += x[k]
    return s

maxVal = 0

