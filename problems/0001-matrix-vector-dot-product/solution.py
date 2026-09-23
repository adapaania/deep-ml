def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	result = []

	for row in a:
		if len(row)!=len(b):
			return(-1)
	
		total = 0
		for i in range(len(b)):
			total +=row[i]*b[i]
		result.append(total)
	return result