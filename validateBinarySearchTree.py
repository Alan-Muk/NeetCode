## given the root of a tree, determine if it is a valid binary search tree
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def validSearchTree(self, root:TreeNode):

		def valid(node, left,right):
			if not node:
				return True

			if not (node.val < right and node.val > left):
				return False

			return (valid(node.left, left, node.val) and
					valid(node.right, node.val, right))

		return valid(root, float("-inf"), float("inf"))