# Problem no. 1293
# Website : https://acm.timus.ru/

# Hint : N rectangular panels, which dimensions are A by B meters. 
#      : 1 square meter needs 1 nanogram of sulphide.
#      : Panels need processing of both sides.

n,a,b = list(map(int, input().split()))
print(2*n*a*b)