def alien_family_tree(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return alien_family_tree(n-1) + alien_family_tree(n-2) 
    
n = int(input())
print(alien_family_tree(n+1))