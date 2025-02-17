func findSpecialInteger(arr []int) int {
	n := len(arr)
	m := n / 4

	for i := 0; i < n; i++ {
		if arr[i] == arr[i+m] {
			return arr[i]
		}
	}
	return 0
}