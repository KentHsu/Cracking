import numbers
from collections import abc


class ListNode:

	def __init__(self, value, node=None):
		if isinstance(value, numbers.Real):
			self.value = value
			self.next = node
		elif isinstance(value, abc.Sequence):
			self.value = value[0]
			self.next = None
			for val in value[1:]:
				self.append_to_tail(val)
		else:
			raise TypeError(f"can't not initialize with {type(value)}")

	def __iter__(self):
		curr = self
		while curr:
			yield curr
			curr = curr.next

	def __str__(self):
		values = [str(node.value) for node in self]
		return " -> ".join(values)

	def __eq__(self, other):
		values = [node.value for node in self]
		other_values = [node.value for node in other]
		return values == other_values

	def append_to_tail(self, value):
		curr = self
		while curr.next:
			curr = curr.next
		curr.next = ListNode(value)


class Node:

	def __init__(self, value, node=None):
		self.value = value
		self.next = node
	
	def __str__(self):
		return f"{self.value}"
	

class LinkedList:
	
	def __init__(self, values):
		self.head = None
		for val in list(values):
			self.append_to_tail(val)
	
	def __iter__(self):
		current = self.head
		while current:
			yield current
			current = current.next

	def __str__(self):
		values = [str(x) for x in self]
		return ' -> '.join(values)
	
	def __eq__(self, other_list):
		return all(curr.value == other.value
					for curr, other in zip(self, other_list))
	
	def append_to_tail(self, value):
		if self.head is None:
			self.head = Node(value, None)
			return
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = Node(value, None)


if __name__ == "__main__":
	mylist = LinkedList((1, 2, 3))
	mylist2 = LinkedList([1, 2, 3])
	mylist3 = LinkedList((2, 4, 7))
	print(mylist, ' and ', mylist2, ' and ', mylist3)
	print(mylist == mylist2)
	print(mylist == mylist3)
	
	myList = ListNode(0)
	myList.append_to_tail(1)
	myList.append_to_tail(2)
	myList.append_to_tail(3)
	myList.append_to_tail(4)
	print(myList)

	myList2 = ListNode([0, 1, 2, 3])
	print(myList2)
	print(myList == myList2)
