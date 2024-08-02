def max_visible_trees():
    n = int(input())
    heights = list(map(int, input().split()))
    
    dp = [1] * n  # Each tree can be seen by itself
    
    for i in range(1, n): #loop check each tree with other trees
        for j in range(i):
            #check if tree i is taller than tree j, the one next to it.
            if heights[i] > heights[j]: 
                #keep track of the maximum number of visible trees when including tree i
                dp[i] = max(dp[i], dp[j] + 1)
    
    print(max(dp))

# Call the function to execute
max_visible_trees()
