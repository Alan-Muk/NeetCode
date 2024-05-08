class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def reverseList(self, head:ListNode) -> ListNode:
		prev, cur = None, head

		while cur:
			nxt = cur.next
			curr.next = prev
			cur = nxt
		return prev