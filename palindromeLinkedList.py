### given a linked list, determine if it's a palindrome
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def isPalindrome(self, head:ListNode) -> bool:
		nums = []

		while head:
			nums.append(head.val)
			head = head.next

		l, r = 0, len(nums) - 1

		while l <= r:
			if nums[l] != nums[r]:
				return False
			l += 1
			r -= 1
		return True 


class Solution:
	def isPalindrome(self, head:ListNode) -> bool:
		fast = head
		slow = head

		## get slow to middle
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next

		## revers middle to end
		prev = None
		while slow:
			tmp = slow.next
			slow.next = prev
			prev = slow
			slow = tmp

		## check if palindrome
		left, right = head, perv
		while right:
			if left.val != right.val:
				return False
			left = left.next
			right = right.next
		return True