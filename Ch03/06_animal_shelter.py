import unittest
from collections import namedtuple


Dog = namedtuple('Dog', 'name')
Cat = namedtuple('Cat', 'name')


class AnimalShelter:
	
	def __init__(self):
		self.queue = []

	def enqueue(self, animal):
		self.queue.append(animal)
	
	def dequeue(self, request=None):
		if request:
			for i in range(len(self.queue)):
				if isinstance(self.queue[i], request):
					animal = self.queue[i]
					break
			self.queue = self.queue[:i] + self.queue[i+1:]
			return animal
		else:
			return self.queue.pop(0)

	def dequeue_any(self):
		return self.dequeue(None)

	def dequeue_dog(self):
		return self.dequeue(Dog)
	
	def dequeue_cat(self):
		return self.dequeue(Cat)


class TestQustion006(unittest.TestCase):
	
	def setUp(self):
		self.shelter = AnimalShelter()
		animals = [Dog('dog1'), Cat('cat1'), Dog('dog2'), Cat('cat2')]
		for animal in animals:
			self.shelter.enqueue(animal)
	
	def tearDown(self):
		pass

	def test_animal_shelter(self):
		self.assertEqual(self.shelter.dequeue_cat(), Cat('cat1'))
		self.assertEqual(self.shelter.dequeue_any(), Dog('dog1'))
		self.assertEqual(self.shelter.dequeue_dog(), Dog('dog2'))


if __name__ == "__main__":
	unittest.main()

