func numSquares(n int) int {
	// dp[i] 表示组成i需要的最少平方数
	// dp[i] = min(dp[i], dp[i - j * j] + 1)
	// j * j <= 1，j是整数
	dp := make([]int, n+1)
	for i := range n + 1 {
		dp[i] = i
		for j := 1; j*j <= i; j++ {
			dp[i] = min(dp[i], dp[i-j*j]+1)
		}
	}

	return dp[n]
}