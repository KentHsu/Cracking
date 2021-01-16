import unittest
from LinkedList import ListNode


def intersection(nodes1, nodes2):
	slow = nodes1
	while slow:
		fast = nodes2
		while fast:
			if fast == slow:
				return True
			fast = fast.next
		slow = slow.next
	return False


class TestQustion007(unittest.TestCase):
	
	dataT = [(ListNode("abcxyz"), ListNode("uvwxyz"))]
	dataF = [(ListNode("abcde"), ListNode("uvwxyz"))]

	def test_intersection(self):
		for test_node1, test_node2 in self.dataT:
			self.assertTrue(intersection(test_node1, test_node2))
		for test_node1, test_node2 in self.dataF:
			self.assertFalse(intersection(test_node1, test_node2))


if __name__ == "__main__":
	unittest.main()

