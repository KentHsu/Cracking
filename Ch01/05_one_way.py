import unittest

def check_one_way(long_str, short_str):
	char_diff = 0
	for char in long_str:
		if char not in short_str:
			char_diff += 1
	return char_diff <= 1

def one_way(string1, string2):
	length_diff = len(string1) - len(string2)
	if length_diff in (0, 1):
		return check_one_way(string1, string2)
	elif length_diff == -1:
		return check_one_way(string2, string1)
	else:
		return False


class TestQuestion005(unittest.TestCase):

	data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

	def test_one_way(self):
		for test_str1, test_str2, result in self.data:
			self.assertEqual(one_way(test_str1, test_str2), result)


if __name__ == "__main__":
	unittest.main()

