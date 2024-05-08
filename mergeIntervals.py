## given a n array of intervals where intervals[i] = [start,end] merge all overlapping intervals and return an array of the non-overlapping intervals

class Solution:
	def merge(self, intervals:list[list[int]]) -> list[list[int]]:
		intervals.sort(key = lambda i : i[0])
		output = [intervals[0]]

		for start, end in intervals[1:]:
			lastEnd = output[-1][1]

			if start <= lastEnd:
				output[-1][1] = max(lastEnd, end)
			else:
				output.append([start,end])

		return output