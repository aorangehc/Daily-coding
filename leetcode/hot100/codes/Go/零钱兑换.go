func coinChange(coins []int, amount int) int {
	// dp[i] 表示凑成i需要的最少零钱数
	dp := make([]int, amount+1)

	// 初始化 dp 数组，设置一个不可能的最大值（amount + 1）
	for i := 1; i <= amount; i++ {
		dp[i] = amount + 1
	}

	dp[0] = 0

	for i := 1; i <= amount; i++ {
		for _, coin := range coins {
			if coin <= i && dp[i-coin] < amount {
				dp[i] = min(dp[i], dp[i-coin]+1)
			}
		}
	}

	if dp[amount] <= amount {
		return dp[amount]
	}

	return -1
}