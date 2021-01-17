import unittest
import string


class StackOfPlates:
	
	threshold = 10

	def __init__(self, plates=None):
		self.stack_of_plates = []
		for plate in plates:
			self.push(plate)
	
	def __str__(self):
		stack_string = ""
		for stack in self.stack_of_plates:
			for plate in stack:
				stack_string += plate
			stack_string += '\n'
		return stack_string
	
	def push(self, value):
		if not self.stack_of_plates or \
		   len(self.stack_of_plates[-1]) == self.threshold:
			self.stack_of_plates.append([value])
		else:
			self.stack_of_plates[-1].append(value)

	def pop(self):
		value = self.stack_of_plates[-1].pop()
		if len(self.stack_of_plates[-1]) == 0:
			self.stack_of_plates.pop()
		return value

	def pop_at(self, index):
		return self.stack_of_plates[index].pop()


class TestQustion003(unittest.TestCase):
	
	def test_stack_of_plates(self):
		my_stack = StackOfPlates(string.ascii_letters)
		print(my_stack)
		self.assertEqual(my_stack.pop(), 'Z')
		for i in range(25):
			my_stack.pop()
		print(my_stack)
		self.assertEqual(my_stack.pop_at(0), 'j')
		print(my_stack)


if __name__ == "__main__":
	unittest.main()

