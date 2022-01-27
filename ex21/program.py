def es21(matrix: list) -> list:
	"""
	 Design function es21(matrix) that takes as input a matrix of
	 characters represented by a list of character lists and returns a
	 new matrix where the columns of the input matrix are
	 alphabetically ordered. At the end of the function, the input
	 matrix should not be modified.

	 For example, if the input matrix is
	 [['q','s','g','g'],
	  ['b','a','m','f'],
	  ['a','b','n','z']]

	the function will return the matrix:
	 [['a','a','g','f'],
	  ['b','b','m','g'],
	  ['q','s','n','z']]

	"""

	col_len = len(matrix)
	new_matrix = [list() for _ in range(col_len)]

	for j in range(len(matrix[0])):
		col_sorted = sorted(matrix[i][j] for i in range(col_len))
		for i, char in enumerate(col_sorted):
			new_matrix[i].append(char)

	return new_matrix
