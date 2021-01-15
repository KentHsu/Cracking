import unittest
from LinkedList import ListNode


def sum_lists(nums1, nums2):
	result = ListNode(0)
	end = result
	carry = 0
	while nums1 and nums2:
		sum_value = nums1.value + nums2.value
		summ = sum_value % 10 + carry
		carry = sum_value // 10
		end.next = ListNode(summ)
		end = end.next
		nums1, nums2 = nums1.next, nums2.next

	remain = nums1 or nums2
	if remain:
		end.next = sum_lists(remain, ListNode(carry))
	else:
		if carry:
			end.next = ListNode(carry)
		else:
			end.value += carry
	result = result.next
	return result


class TestQustion005(unittest.TestCase):
	
	data = [
		((ListNode([1, 3, 5]), ListNode([6, 7, 1])), 
		  ListNode([7, 0, 7])),
		((ListNode([1, 3, 5]), ListNode([6, 7, 1, 5])), 
		  ListNode([7, 0, 7, 5])),
		((ListNode([1, 3, 5, 2]), ListNode([6, 7, 1])), 
		  ListNode([7, 0, 7, 2])),
		((ListNode([1, 3, 5, 2]), ListNode([6, 7, 5])), 
		  ListNode([7, 0, 1, 3])),
		((ListNode([1, 3, 7, 9]), ListNode([6, 7, 3])), 
		  ListNode([7, 0, 1, 0, 1])),
		((ListNode(1), ListNode(9)),
		  ListNode([0, 1])),
		((ListNode([1]), ListNode([9, 9, 9])), 
		  ListNode([0, 0, 0, 1])),
	]

	def test_sum_lists(self):
		for test_case, result in self.data:
			test_list = sum_lists(test_case[0], test_case[1])
			self.assertEqual(test_list, result)


if __name__ == "__main__":
	unittest.main()

