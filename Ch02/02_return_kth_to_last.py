import unittest
from LinkedList import ListNode


def return_kth_to_last(nums, k):
	count = 0
	runner = nums
	while count < k:
		runner = runner.next
		count += 1
	curr = nums
	while runner:
		curr = curr.next
		runner = runner.next
	return curr 


class TestQustion002(unittest.TestCase):
	
	data = [(ListNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 
			 ListNode([5, 6, 7, 8, 9, 10]))]
	
	def test_return_kth_to_last(self):
		for test_case, result in self.data:
			test_list = return_kth_to_last(test_case, 6)
			self.assertEqual(test_list, result) 
	

if __name__ == "__main__":
	unittest.main()

