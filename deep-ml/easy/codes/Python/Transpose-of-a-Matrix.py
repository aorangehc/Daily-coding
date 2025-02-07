def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	b = []

	for i in range(len(a[0])):
		temp = []
		for j in range(len(a)):
			temp.append(a[j][i])
		b.append(temp)
	return b