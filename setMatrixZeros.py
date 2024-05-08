## given an m x n martix, if an element is 0, set its entire row and column to 0

class Solution:
	def setZeros(self, matrix:list[list[int]]) -> None:
		ROW,COLS = len(matrix), len(matrix[0])
		rowZero = False

		for r in ROW:
			for c in COLS:
				if matrix[r][c] == 0:
					matrix[0][c] = 0

					if r > 0:
						matrix[r][0] = 0
					else:
						rowZero = True

		for r in range(1, ROW):
			for c in range(1, COLS):
				if matrix[0][c] == 0 or matrix[r][0] == 0:
					matrix[r][0] = 0

		if matrix[0][0] == 0:
			for r in range(ROW):
				matrix[r][0] = 0

		if rowZero:
			for c in range(COLS):
				matrix[0][c] = 0