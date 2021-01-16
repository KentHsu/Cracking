import unittest
from LinkedList import ListNode


def loop_detection(nodes):
	try:
		slow, fast = nodes, nodes
		while True:
			slow = slow.next
			fast = fast.next.next
			if slow.value == fast.value:
				break

		slow = nodes
		while slow.value != fast.value:
			slow = slow.next
			fast = fast.next
		return slow
	except AttributeError:
		return None
	

def loop_detection2(nodes):
	slow, fast = nodes, nodes
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if fast and slow.value == fast.value:
			break

	if fast is None:
		return None
	else:
		slow = nodes
		while slow.value != fast.value:
			slow = slow.next
			fast = fast.next
		return slow


class TestQustion008(unittest.TestCase):
	
	cycle_nodes = ListNode("abcxyz")
	end = cycle_nodes
	while end.next:
		end = end.next
	end.next = cycle_nodes.next

	dataT = [(cycle_nodes, "b")]
	dataF = [(ListNode("abcxyz"), None)]

	def test_loop_detection(self):
		for test_nodes, result in self.dataT:
			test_result = loop_detection2(test_nodes)
			self.assertEqual(test_result.value, result)
		for test_nodes, result in self.dataF:
			test_result = loop_detection2(test_nodes)
			self.assertEqual(test_result, result)


if __name__ == "__main__":
	unittest.main()

