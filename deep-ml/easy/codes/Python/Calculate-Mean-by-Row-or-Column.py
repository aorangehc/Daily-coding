def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	len_col = len(matrix)
	len_row = len(matrix[0])
	if mode == 'column':
		for i in range(len_row):
			temp = 0
			for j in range(len_col):
				temp += matrix[j][i]
			means.append(temp / len_col)
	else:
		for row in matrix:
			means.append(sum(row) / len_row)
	return means