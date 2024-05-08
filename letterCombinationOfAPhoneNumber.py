## given a string containing digits from 2-9 inclusive, return all posible letter combinations
 
class Solution:
 	def letterCombinations(self, digits:str) -> list[str]:
 		res = []
 		digitToCahr = { "2":"abc",
 						"3":"def",
 						"4":"ghi",
 						"5":"jkl",
 						"6":"mno",
 						"7":"pqrs",
 						"8":"tuv",
 						"9":"wxyz" } 

 		def backtrack(i, curStr):
 			if len(curStr) == len(digits):
 				res.append(curStr)
 				return

 			for c in digitToCahr[digits[i]]:
 				backtrack(i + 1, curStr + c)

 		if digits:
 			backtrack(0, "")

 		return res