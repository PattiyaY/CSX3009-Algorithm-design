# Problem no. 1409
# Website : https://acm.timus.ru/

# Hint : The number of cans shot by Harry and by Larry respectively.
#      : At some moment it happened so that they shot one and the same can.

harry, larry = list(map(int, input().split()))
total_cans = harry+larry-1
print(total_cans-harry, total_cans-larry)