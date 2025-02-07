def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	len_a = len(a[0])
	len_b = len(b)

	if len_a != len_b:
		return -1

	c = list()

	for raw in a:
		temp = 0
		for i in range(len_b):
			temp += raw[i] * b[i]
		c.append(temp)

	return c