import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
	a = np.array(a)
	b = np.array(b)

	if len(a[0]) != len(b):
		return -1

	c = np.dot(a, b)

	return c.tolist()