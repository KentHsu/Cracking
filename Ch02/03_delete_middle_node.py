import unittest
from LinkedList import ListNode


def delete_middle_node(nums, val):
	curr = nums
	while curr.next:
		if curr.next.value == val:
			curr.next = curr.next.next
			break
		curr = curr.next


class TestQustion003(unittest.TestCase):
	
	data = [(ListNode([1, 2, 5, 9, 12, 17, 20]), 
			 ListNode([1, 2, 9, 12, 17, 20]))]

	def test_delete_middel_node(self):
		for test_case, result in self.data:
			delete_middle_node(test_case, 5)
			self.assertEqual(test_case, result)


if __name__ == "__main__":
	unittest.main()

