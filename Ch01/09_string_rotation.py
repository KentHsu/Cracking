import unittest

def is_substring(string, sub):
	return string.find(sub) != -1

def string_rotation(str1, str2):
	if len(str1) == len(str2) != 0:
		return is_substring(str1 + str1, str2)
	return False

def string_rotation2(str1, str2):
	if len(str1) != len(str2):
		return False
	else:
		for i in range(1, len(str1)):
			if is_substring(str2, str1[:i]):
				return True
		return False


class TestQuestion009(unittest.TestCase):

	dataT= [('waterbottle', 'erbottlewat'), ('barfoo', 'foobar')]
	dataF = [('waterbottle', 'erbottlewa'), ('foo', 'bar')]

	def test_string_rotation(self):
		for str1, str2 in self.dataT:
			self.assertTrue(string_rotation(str1, str2))
		for str1, str2 in self.dataF:
			self.assertFalse(string_rotation(str1, str2))
	

if __name__ == "__main__":
	unittest.main()

