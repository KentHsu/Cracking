import unittest
from LinkedList import ListNode


def palindrome(nums):
	slow, fast = nums, nums
	palindrome = []
	while fast and fast.next:
		palindrome.append(slow.value)
		slow = slow.next
		fast = fast.next.next

	if fast is not None:
		palindrome.append(slow.value)
	while slow:
		if slow.value != palindrome.pop():
			return False
		slow = slow.next
	return True

class TestQustion006(unittest.TestCase):
	
	dataT = [ListNode("abcba"), ListNode("abccba")]
	dataF = [ListNode("abcde"), ListNode("uvwxyz")]

	def test_palindrome(self):
		for test_case in self.dataT:
			self.assertTrue(palindrome(test_case))
		for test_case in self.dataF:
			self.assertFalse(palindrome(test_case))


if __name__ == "__main__":
	unittest.main()

