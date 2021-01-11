import unittest

def is_unique(string):
	if len(string) > 128:
		return False
	
	char_set = [False for _ in range(128)]
	for char in string:
		val = ord(char)
		if char_set[val]:
			return False
		char_set[val] = True
	return True

def is_unique_1(string):
	table = set()
	for char in string:
		if char in table:
			return False
		table.add(char)
	return True

class TestQustion001(unittest.TestCase):
	
	dataT = [('abcd'), ('s4fad'), ('')]
	dataF = [('23ds2'), ('hb 627jh=j ()')]

	def test_unique(self):
		for test_case in self.dataT:
			self.assertTrue(is_unique_1(test_case))
		for test_case in self.dataF:
			self.assertFalse(is_unique_1(test_case))


if __name__ == "__main__":
	unittest.main()

