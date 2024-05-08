## given a string text, you want to use the characters to form as many instances of the word balloon as possible

class Solution:
	def maxNumberOfBalloons(self, text:str) -> int:
		countText = Counter(text)
		balloon = Counter("balloon")

		res = len(text)
		for c in balloon:
			res = min(res, countText[c] // balloon[c])
		return res