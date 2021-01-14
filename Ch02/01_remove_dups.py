import unittest
from LinkedList import ListNode


def remove_dups(nums):
	table = set()
	curr = nums
	while curr:
		table.add(curr.value)
		if curr.next and curr.next.value in table:
			curr.next = curr.next.next
		curr = curr.next

def remove_dups_without_table(nums):
	curr = nums
	while curr:
		runner = curr
		while runner:
			if runner.next and runner.next.value == curr.value:
				runner.next = runner.next.next
			runner = runner.next
		curr = curr.next


class TestQustion001(unittest.TestCase):
	
	data = [(ListNode([1, 5, 1, 10, 3, 6, 6, 9]), 
			 ListNode([1, 5, 10, 3, 6, 9]))]

	def test_remove_dups(self):
		for test_case, result in self.data:
			remove_dups_without_table(test_case)
			self.assertEqual(test_case, result)


if __name__ == "__main__":
	unittest.main()

