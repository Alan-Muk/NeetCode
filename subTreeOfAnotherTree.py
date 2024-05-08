## given the roots of two binary trees, return true if there subtree of root with the same structure

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left=left
		self.right = right

class Solution:
	def isSubTree(self, s:TreeNode, t:TreeNode) -> bool:
		if not t: return True
		if not s: return False

		if self.sameTree(s,t):
			return True

		return (self.isSubTree(s.left, t) or
			self.isSubTree(s.right, t))


	def sameTree(self, s, t):
		if not s and not t: return True

		if s and t and s.val == t.val:
			retrun (self.sameTree(s.left, t.left) and
				self.sameTree(s.right, t.right))

		return False