## given m x n binary matrix find the largest square containing only 1's and return it's area

class Solution:
	def maximalSquare(self, matrix:list[list[str]]) -> int:
		ROWS, COLS = len(matrix), len(matrix[0])
		cache = {}

		def helper(r,c):
			if r >= ROWS or c >= COLS:
				return 0

			if (r,c) not in cache:
				down = helper(r+1, c)
				right = helper(r, c+1)
				diag = helper(r+1, c+1)

				cache[(r,c)] = 0
				if matrix[r][c] == "1":
					cache[(r,c)] = 1 + min(down, right, diag)

			return cache[(r,c)]

		helper(0,0)
		
		return max(cache.values()) ** 2