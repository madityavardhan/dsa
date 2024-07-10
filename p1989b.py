def lcs(a, b):
    # Create a DP table to store lengths of longest common subsequence
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[len(a)][len(b)]

t = int(input())
for _ in range(t):
    a = input()
    b = input()
    
    lcs_length = lcs(a, b)
    min_length = len(a) + len(b) - lcs_length
    
    print(min_length)
