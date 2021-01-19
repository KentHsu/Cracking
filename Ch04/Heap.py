
class MinHeap:

	def __init__(self, heap=None):
		self.heap = []
		for value in list(heap):
			self.push(value)
	
	def heapify(self):
		for i in range(len(self.heap)-1, 0, -1):
			j = (i - 1) // 2
			if self.heap[j] > self.heap[i]:
				self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def push(self, value):
		self.heap.append(value)
		self.heapify()
	
	def pop(self):
		if len(self.heap) == 0:
			raise IndexError("Can't pop from empty heap")
		value = self.heap[0]
		self.heap = self.heap[1:]
		self.heapify()
		return value


def isHeap(heap):
	for i in range(len(heap)):
		try:
			for j in (2 * i + 1, 2 * i + 2):
				if heap[i] > heap[j]:
					return False
		except IndexError:
			pass
	return True

	
if __name__ == '__main__':
	data = list(range(1, 10))[::-1]
	my_heap = MinHeap(data)
	print(my_heap.heap)
	print(isHeap(my_heap.heap))
	my_heap.push(0)
	print(my_heap.heap)
	print(isHeap(my_heap.heap))
	my_value = my_heap.pop()
	print(my_value)
	print(my_heap.heap)
	print(isHeap(my_heap.heap))

