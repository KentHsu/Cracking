import unittest


class MyStack:
	
	def __init__(self, stack=None):
		self.stack = stack
	
	def __str__(self):
		return str(self.stack)

	def push(self, value):
		return self.stack.append(value)

	def pop(self):
		return self.stack.pop()

	def peek(self):
		return self.stack[-1]

	def isEmpty(self):
		return len(self.stack) == 0


def sort_stack(stack):
	temp_stack = MyStack([])
	while not stack.isEmpty():
		value = stack.pop()
		while not temp_stack.isEmpty() and temp_stack.peek() > value:
			stack.push(temp_stack.pop())
		temp_stack.push(value)
	
	while not temp_stack.isEmpty():
		stack.push(temp_stack.pop())
	
		
class TestQustion005(unittest.TestCase):
	
	def test_sort_stack(self):
		my_stack = MyStack([1, 3, 5, 4, 6, 2])
		sort_stack(my_stack)
		self.assertEqual(my_stack.pop(), 1)
		self.assertEqual(my_stack.pop(), 2)
		self.assertEqual(my_stack.pop(), 3)


if __name__ == "__main__":
	unittest.main()

