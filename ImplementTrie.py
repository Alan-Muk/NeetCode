## a trie or prefix tree is a tree data structure that stores strings
class TrieNode:
	def __init__(self):
		self.children = {}
		self.endOfWord = False



class Trie:

	def __init__(self):
		self.root = TrieNode()

	def insert(self, word:str) -> None:
		cur = self.root

		for c in word:
			if c not in cur.children:
				cur.children[c] = TrieNode()
			cur = cur.children[c]
		cur.endOfWord = True

	def search(self, word:str) -> bool:
		cur = self.root

		for c in word:
			if c not in cur.children:
				return False
			cur = cur.children[c]
		return cur.endOfWord

	def startWith(self, prefix:str) -> bool:
		cur = self.root

		for c in prefix:
			if c not in cur.children:
				return False
			cur = cur.children[c]
		return True