## given an n x n 2D matrix representing an image, rotate the image by 90(clockwise)

class Solution:
	def rotateImage(self, matrix:list[list[int]]) -> None:
		l, r = 0, len(matrix) -1

		while l < r:
			for i in range(r - l):
				top, bottom = l, r

				#topleft value
				topLeft = matrix[top][l + i]
				matrix[top][l + i] = matrix[bottom - i][l]
				matrix[bottom - i][l] = matrix[bottom][r - i]
				matrix[bottom][r - i] = matrix[top + i][r]
				matrix[top + i][r] = topLeft

			r -= 1
			l += 1