import unittest

def check_permutation(string1, string2):
	string1_dict = {}
	for char in string1:
		string1_dict[char] = string1_dict.get(char, 0) + 1
	for char in string2:
		if string1_dict.get(char, 0) == 0:
			return False
		else:
			string1_dict[char] -= 1
	return True


def check_permutation_1(string1, string2):
	return sorted(string1) == sorted(string2)
	

class TestQuestion002(unittest.TestCase):
	
	dataT = (
		('abcd', 'bacd'), 
		('3563476', '7334566'), 
		('wef34f', 'wffe34')
	)

	dataF = (
		('abcd', 'd2cba'), 
		('2354', '1234'), 
		('dcw4f', 'dcw5f')
	)

	def test_check_permutation(self):
		for test_case in self.dataT:
			self.assertTrue(check_permutation(*test_case))
		for test_case in self.dataF:
			self.assertFalse(check_permutation(*test_case))


if __name__ == "__main__":
	unittest.main()

