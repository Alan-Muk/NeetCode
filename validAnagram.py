### two strings s and t return true if t is an anagram of s
class Solution:
	def isAnagram(self, s:str, t:str) -> bool: 

		# check length
		if len(s) != len(t):
			return False
		#initialize hashMap
		countS, countT = {}, {}
		#load hashMap
		for i in range(len(s)):
			countS[s[i]] = 1 + countS.get(s[i], 0)
			countT[t[i]] = 1 + countT.get(t[i], 0)
		#compare hashMap
		for c in countS:
			if countS[c] != countT.get(c, 0):
				return False
		return True

