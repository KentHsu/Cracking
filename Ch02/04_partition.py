import unittest
from LinkedList import ListNode


def partition(nums, val):
	left, right = ListNode(0), ListNode(0)
	left_end, right_end = left, right
	curr = nums
	while curr:
		if curr.value < val:
			left_end.next = curr
			left_end = left_end.next	
		else:
			right_end.next = curr
			right_end = right_end.next
		curr = curr.next
	left, right = left.next, right.next
	right_end.next = None
	left_end.next = right
	return left

def partition2(nums, val):
	head, tail = nums, nums
	while nums:
		next_node = nums.next
		if nums.value < val:
			nums.next = head
			head = nums
		else:
			tail.next = nums
			tail = nums
		nums = next_node
	tail.next = None
	print(head)
	return head


class TestQustion004(unittest.TestCase):
	
	data1 = [(ListNode([3, 5, 8, 5, 10, 2, 1]), 
			 ListNode([3, 2, 1, 5, 8, 5, 10]))]
	data2 = [(ListNode([3, 5, 8, 5, 10, 2, 1]), 
			 ListNode([1, 2, 3, 5, 8, 5, 10]))]

	def test_partition(self):
		for test_case, result in self.data2:
			test_list = partition2(test_case, 5)
			self.assertEqual(test_list, result)


if __name__ == "__main__":
	unittest.main()

