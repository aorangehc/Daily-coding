def solution(n, k, data):
    # Edit your code here
    # 当前可以选择买0-k个，需要消耗一个
    # 通过消耗设计状态转移方程
    # dp[i][j] 表示第i个补给站保留j份食物最小花费
    # 还要确保能够每天都有食物吃
    # 第一天是必须要买的

    
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]

    for j in range(1, k + 1):
        dp[1][j] = data[0] * j
    
    for i in range(2, n + 1):
        for j in range(k + 1):
            for x in range(j + 1):
                if j - x + 1 >= 0 and j - x + 1 <= k:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-x+1] + x * data[i-1])  


    return dp[n][1]


if __name__ == "__main__":
    # Add your test cases here

    print(solution(5, 2, [1, 2, 3, 3, 2]) )
