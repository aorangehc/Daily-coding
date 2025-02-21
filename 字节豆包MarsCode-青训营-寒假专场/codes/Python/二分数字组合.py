def solution(n, A, B, array_a):
    # 先求整体和的个位数all_mod，判断(A+B)%10是否等于all_mod
    # 然后判断all_mod是否等于A或B，如果是直接返回1，A和B都是个位数，如果相等不会有其他结果
    # 最后进行动态规划，设计dp[i][j],表示前i个数，和的个位数为j的情况
    # 初始化，不选任何数时，和的个位数为0 : dp[0][0] = 1
    # 如果选当前第i个数，dp[i][j] += dp[i - 1][(j - array_a[i - 1] + 10) % 10]
    # 如果不选当前第i个数，dp[i][j] += dp[i - 1][j]
    # 最后dp[n][A] 就是结果

    all_sum = sum(array_a)
    all_mod = all_sum % 10
    if all_mod == A or all_mod == B:
        return 1
    if all_mod != (A + B) % 10:
        return 0

    dp = [[0 for _ in range(10)] for _ in range(n + 1)]

    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(10):
            dp[i][j] += dp[i - 1][j]
            dp[i][j] += dp[i - 1][(j - array_a[i - 1] + 10) % 10]

    return dp[n][A]

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(3, 1, 2, [1,1,1]))
    print(solution(3, 3, 5, [1,1,1]) == 1 )
    print(solution(2, 1, 1, [1,1]) == 2 )