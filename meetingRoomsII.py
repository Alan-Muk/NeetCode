## given an array of meeting intervals consisting of start and end times, find the minimum number of rooms required

class Interval:
	def __init__(self, start, end):
		self.start = start
		self.end = end

class Solution:
	def minMeetingRooms(self, intervals):
		start = sorted([ i.start for i in intervals])
		end = sorted([ i.end for i in intervals])

		res, count = 0, 0
		s,e = 0, 0

		while s < len(intervals):
			if start[s] < end[e]:
				s += 1
				count += 1

			else:
				e += 1
				count -= 1
			res = max(res, count)
		return res