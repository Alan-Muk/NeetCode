## given an array, replace every value with the greatest element to its right

class Solution:
	def replaceElements(self, arr:list[int]) -> list[int]:
		rightMax = -1

		for i in range(len(arr) - 1, -1, -1):
			newMax = max(rightMax, arr[i])
			arr[i] = rightMax
			rightMax = newMax
		return arr