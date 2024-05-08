## reverse a linked list

## iteratively, using pointers
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next= next

class Solution:
	def reverseList(self, head:ListNode) -> ListNode:
		prev, curr = None, head

		while curr:
			nxt = curr.next
			curr.next = prev
			prev = curr
			curr = nxt
		return prev

## recursive

class Solution:
	def reverseList(self, head:ListNode) -> ListNode:
		if not head:
			return None

		newHead = head
		if head.next:
			newHead = self.reverseList(head.next)
			head.next.next = head
		head.next = None
		
		return newHead