## given the root of a binary tree, construct a string with preorder traversal

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def tree2str(self, root:TreeNode) -> str:
		res = []

		def preorder(root):
			if not root:
				return

			res.append("(")
			res.append(str(root.val))

			if not root.left and root.right:
				res.append("()")
			preorder(root.left)
			preorder(root.right)

			res.append(")")

		preorder(root)
		return "".join(res)[1:-1]
