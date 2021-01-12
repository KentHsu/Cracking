import unittest


def palindrome_permutation(string):
	table = set() 
	for char in string.lower():
		if char != ' ':
			if char in table:
				table.discard(char)
			else:
				table.add(char)
	return len(table) <= 1


class TestQuestion004(unittest.TestCase):

	dataT = [
		'Tact Coa', 
		'jhsabckuj ahjsbckj', 
		'Able was I ere I saw Elba', 
		'no x in nixon', 'azAZ'
	]
	
	dataF = [
		'So patient a nurse to nurse a patient so', 
		'Random Words', 
		'Not a Palindrome'
	]

	def test_palindrome_permutation(self):
		for test_case in self.dataT:
			try:
				self.assertTrue(palindrome_permutation(test_case))
			except AssertionError:
				print(test_case)
		for test_case in self.dataF:
			self.assertFalse(palindrome_permutation(test_case))


if __name__ == "__main__":
	unittest.main()

