## you are given a string s and a single integer k, you can choose any character of the string an dcnage it to any other character at most k times. Return length of the longest substring containing the same letter

class Solution:
	def characterReplacement(self, s:str, k:int) -> int:
		count = {}
		res = 0

		l = 0
		for r in range(len(s)):
			count[s[r]] = 1 + count.get(s[r], 0)

			while (r - l +1) - max(count.values()) > k:
				counr[s[l]] -= 1

			res = max(res, r-1 +1)
		return res