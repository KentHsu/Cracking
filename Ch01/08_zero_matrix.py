import unittest

def zero_matrix(matrix):
	row_table = set()
	col_table = set()
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] == 0:
				row_table.add(i)
				col_table.add(j)
	
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if i in row_table or j in col_table:
				matrix[i][j] = 0


class TestQuestion008(unittest.TestCase):

	data = (
			([[1, 2, 3], [4, 0, 6], [7, 8, 9]], 
			 [[1, 0, 3], [0, 0, 0], [7, 0, 9]]),
			([[1, 2, 3, 4, 0],
             [6, 0, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 0, 18, 19, 20],
             [21, 22, 23, 24, 25]], 
			 [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [11, 0, 13, 14, 0],
             [0, 0, 0, 0, 0],
             [21, 0, 23, 24, 0]])
	)

	def test_zero_matrix(self):
		for test_case in self.data:
			matrix, result = test_case
			zero_matrix(matrix)
			self.assertEqual(matrix, result)


if __name__ == "__main__":
	unittest.main()

