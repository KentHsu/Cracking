import unittest

def rotate_matrix(matrix):
	n = len(matrix)
	for i in range(n//2):
		for j in range(i, n-i-1):
			temp = matrix[i][j]
			matrix[i][j] = matrix[n-j-1][i]
			matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
			matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
			matrix[j][n-i-1] = temp
	return matrix


class TestQuestion007(unittest.TestCase):

	data = [
		([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
		 [[7, 4, 1], [8, 5, 2], [9, 6, 3]]), 
		([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
		 [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]])
	]

	def test_rotate_matrix(self):
		for test_case, result in self.data:
			self.assertEqual(rotate_matrix(test_case), result)


if __name__ == "__main__":
	unittest.main()

