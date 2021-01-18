import unittest


class QueueViaStacks:
	
	def __init__(self, queue=None):
		self.new_stack = []
		self.old_stack = []
		for value in queue:
			self.add(value)

	def add(self, value):
		self.new_stack.append(value)

	def _move_stack(self):
		if len(self.old_stack) == 0:
			while self.new_stack:
				self.old_stack.append(self.new_stack.pop())

	def remove(self):
		self._move_stack()
		return self.old_stack.pop()

	def peek(self):
		self._move_stack()
		value = self.old_stack.pop()
		self.old_stack.append(value)
		return value

	def isEmpty(self):
		size = len(self.new_stack) + len(self.old_stack)
		return size == 0


class TestQustion004(unittest.TestCase):
	
	def test_queue_via_stack(self):
		my_stack = QueueViaStacks([1, 2, 3])
		self.assertEqual(my_stack.remove(), 1)
		self.assertEqual(my_stack.peek(), 2)
		self.assertFalse(my_stack.isEmpty())
		my_stack.remove()
		my_stack.remove()
		self.assertTrue(my_stack.isEmpty())


if __name__ == "__main__":
	unittest.main()

