import unittest


class StackMin:
	
	def __init__(self, stack=None):
		self.stack = []
		self.stack_min = []
		for value in stack:
			self.push(value)
	
	def push(self, value):
		self.stack.append(value)
		if not self.stack_min or value < self.min():
			self.stack_min.append(value)
		else:
			self.stack_min.append(self.min())

	def pop(self):
		self.stack_min.pop()
		return self.stack.pop()
	
	def min(self):
		if self.stack_min:
			return self.stack_min[-1]
		else:
			return None


class TestQustion002(unittest.TestCase):
	
	def test_stack_min(self):
		my_stack = StackMin([4, 3, 2, 1])
		self.assertEqual(my_stack.pop(), 1)
		self.assertEqual(my_stack.min(), 2)
		my_stack.push(5)
		self.assertEqual(my_stack.min(), 2)
		my_stack.push(0)
		self.assertEqual(my_stack.min(), 0)


if __name__ == "__main__":
	unittest.main()

