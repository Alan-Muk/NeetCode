## given a 2D grid m x n and an integer k, you need to shift the grid k times

class Solution:
	def shiftGrid(self, grid:list[list[int]], k:int) -> list[list[int]]:
		M, N = len(grid), len(grid[0])

		def posToVal(r,c):
			return r * N + c
		def valToPos(v):
			return [v // N, v % N]

		res = [[0] * N for i in range(M)]

		for r in range(M):
			for c in range(N):
				newVal = (posToVal(r,c) + k) % (M * N)
				newR, newC = valToPos(newVal)
				res[newR][newC] = grid[r][c]

		return res