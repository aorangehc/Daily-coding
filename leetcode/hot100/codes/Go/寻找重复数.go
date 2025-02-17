func findDuplicate(nums []int) int {
	slow := 0
	fast := 0
	slow = nums[slow]
	fast = nums[nums[fast]]

	for slow != fast {
		slow = nums[slow]
		fast = nums[nums[fast]]
	}
	slow = 0
	for slow != fast {
		slow = nums[slow]
		fast = nums[fast]
	}

	return slow
}