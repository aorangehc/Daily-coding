def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	len_vectors = len(vectors)
	means = [sum(vector) / len(vector) for vector in vectors]
	
	
	ans = []

	for i in range(len_vectors):
		temp = []
		for j in range(len_vectors):
			cov = 0
			for x, y in zip(vectors[i], vectors[j]):
				cov += (x - means[i]) * (y - means[j])
			cov /= (len(vectors[i]) - 1)
			temp.append(cov)
		ans.append(temp)
	return ans