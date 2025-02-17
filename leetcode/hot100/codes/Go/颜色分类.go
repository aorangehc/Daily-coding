func sortColors(nums []int) {
	ptr_0 := 0
	ptr_2 := len(nums) - 1

	for i := 0; i <= ptr_2; i++ {
		for i < ptr_2 && nums[i] == 2 {
			nums[i], nums[ptr_2] = nums[ptr_2], nums[i]
			ptr_2 -= 1
		}
		if nums[i] == 0 {
			nums[i], nums[ptr_0] = nums[ptr_0], nums[i]
			ptr_0 += 1
		}
	}
}