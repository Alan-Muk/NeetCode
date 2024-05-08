## given the root of a binary search tree and an integer k, return kth smallest element

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def KthSmallest(self, root:TreeNode, k:int) -> int:
		n = 0
		stack = []
		cur = root

		while cur and stack:
			while cur:
				stack.append(cur)
				cur = cur.left
			cur = stack.pop()
			n += 1
			if n == k:
				return cur.val
			cur = cur.right