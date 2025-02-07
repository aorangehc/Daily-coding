def solution(m: int, n: int, p: list[list[int]]) -> int:
    # 创建一个数组来存储到达每一天的最小花费
    dp = [float('inf')] * (m + 1)
    dp[0] = 0  # 第0天的花费为0

    # 创建一个价格数组，方便查找每一天的食物价格
    prices = [float('inf')] * (m + 1)
    for station in p:
        prices[station[0]] = station[1]

    # 动态规划计算每一天的最小花费
    for day in range(1, m + 1):
        for j in range(day):
            if prices[j] != float('inf'):
                dp[day] = min(dp[day], dp[j] + prices[j] * (day - j))

    return dp[m]  # 返回到达第M天的最小花费

if __name__ == "__main__":
    # Add your test cases here

    print(solution(5, 4, [[0, 2], [1, 3], [2, 1], [3, 2]]) == 7)
