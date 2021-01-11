import unittest

def urlify(string, length):
	result = ''
	idx = 0
	while idx < length:
		char = string[idx]
		if char == ' ':
			result += '%20'
		else:
			result += char
		idx += 1
	return result
			

def urlify_1(string):
	return string.strip(' ').replace(' ', '%20')


class TestQustion003(unittest.TestCase):
	
	data = [
		(('much ado about nothing      '), 22,
		('much%20ado%20about%20nothing')),
		(('Mr John Smith   '), 13,
		('Mr%20John%20Smith'))
	]

	def test_urlify(self):
		for test_case, length, answer in self.data:
			self.assertEqual(urlify(test_case, length), answer)


if __name__ == "__main__":
	unittest.main()

