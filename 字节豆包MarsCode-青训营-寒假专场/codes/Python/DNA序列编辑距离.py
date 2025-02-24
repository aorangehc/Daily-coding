def solution(dna1, dna2):
    # 这个问题可以看作字符串的最少变换问题
    n = len(dna1)
    m = len(dna2)

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for j in range(m + 1):
        dp[0][j] = j
    for i in range(n + 1):
        dp[i][0] = i
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dna1[i - 1] == dna2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1)
    
    return dp[n][m]

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("AGCTTAGC", "AGCTAGCT") == 2 )
    print(solution("AGCCGAGC", "GCTAGCT") == 4)