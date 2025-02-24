func nextPermutation(nums []int) {
	n := len(nums) - 1
	i := n - 1

	for i >= 0 && nums[i] >= nums[i+1] {
		i -= 1
	}
	if i >= 0 {
		j := n

		for j >= 0 && nums[i] >= nums[j] {
			j -= 1
		}
		nums[i], nums[j] = nums[j], nums[i]
	}

	left, right := i+1, n

	for left < right {
		nums[left], nums[right] = nums[right], nums[left]
		left++
		right--
	}

}