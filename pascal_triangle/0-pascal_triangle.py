def pascal_triangle(n):
	"""return a list of lists of integers representing the Pascal's triangle"""
	if n <= 0:
		return[]

	triangle = []
	triangle.append([1])

	for i in range(n - 1):
		row = triangle[- 1]
		new = [1]

		for j in range(len(row) - 1):
			new.append(row[j] + row[j+1])

		new.append(1)
		triangle.append(new)
	
	return triangle
