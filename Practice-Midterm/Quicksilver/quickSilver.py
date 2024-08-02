def quickSilver():
    # Read the first line of input
    N, K, S = map(int, input().split())
    
    # Read the positions and scores of the balls
    events = []
    for _ in range(N):
        p, s = map(int, input().split())
        events.append((p, s))
    
    # Initialize the dynamic programming array
    dp = [-float('inf')] * N
    max_score = 0

    # If the starting position is within reach of the first ball, initialize the dp array
    for i in range(N):
        if abs(events[i][0] - S) <= K:
            dp[i] = events[i][1]
            max_score = max(max_score, dp[i])
    
    # Update the dp array considering each ball and previous balls
    for i in range(1, N):
        for j in range(i):
            if abs(events[i][0] - events[j][0]) <= K:
                dp[i] = max(dp[i], dp[j] + events[i][1])
                max_score = max(max_score, dp[i])
    
    print(max_score)

# Test the function with user inputs
quickSilver()
