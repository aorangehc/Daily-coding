func generate(numRows int) [][]int {
	ans := make([][]int, numRows)

	for i := range numRows {
		ans[i] = make([]int, i+1)
		ans[i][0] = 1
		ans[i][i] = 1

		for j := 1; j < i; j++ {
			ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
		}
	}

	return ans
}