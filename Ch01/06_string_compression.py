import unittest

def string_compression(string):
	result = ''
	count = 1
	for idx in range(len(string) - 1):
		if string[idx + 1] == string[idx]:
			count += 1
		else:
			result += (string[idx] + str(count))
			count = 1
	result += (string[idx] + str(count))
	return result if len(result) < len(string) else string


class TestQuestion006(unittest.TestCase):

	data = [('aabccccaaa', 'a2b1c4a3'),
			('aabcd', 'aabcd')]

	def test_string_compression(self):
		for test_case, result in self.data:
			self.assertEqual(string_compression(test_case), result)


if __name__ == "__main__":
	unittest.main()

