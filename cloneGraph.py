## given a refernce of a node in a connected undirected graph, return a deep copy of the graph

class Node:
	def __init__(self, val = 0, neighbors = None):
		self.val = val
		self.neighbors = neighbors if neighbors is not None else []


class Solution:
	def cloneGraph(self, node:Node) -> Node:
		oldToNew = {}

		def dfsClone(node):
			if node in oldToNew:
				return oldToNew[node]

			copy = Node(node.val)
			oldToNew[node] = copy
			for nei in node.neighbors:
				copy.neighbors.append(dfsClone(nei))
			return copy

		return dfsClone(node) if node else None