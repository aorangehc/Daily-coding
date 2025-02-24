func rob(nums []int) int {
	// 两个相邻的房间，只能偷一个，所以当前如果要偷的话，前一个不能偷
	// dp[i] 表示当前的最大值 dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
	dp := make([]int, len(nums))
	dp[0] = nums[0]
	if len(nums) > 1 {
		dp[1] = max(nums[1], nums[0])
	}

	for i := 2; i < len(nums); i++ {
		dp[i] = max(dp[i-1], dp[i-2]+nums[i])
	}

	return dp[len(nums)-1]
}