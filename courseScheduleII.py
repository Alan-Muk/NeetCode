## there are a total of n courses, some courses have some prerequisits, given a total number of courses, return the ordering of courses to toake to finish the course

class Solution:
	def findOrder(self, numCourses:int, prerequisites:list[list[int]]) -> list[int]:
		prereq = {c:[] for c in range(numCourses)}
		for crs, prereq in prerequisites:
			prereq[crs].append(pre)

		output = []
		visit, cycle = set(), set()

		def dfs(crs):
			if crs in cycle:
				return False
			if crs in visit:
				return True

			cycle.add(crs)

			for pre in prereq[crs]:
				if dfs(pre) == False:
					return False
			cycle.remove(crs)
			visit.add(crs)
			output.append(crs)
			return True

		for crs in range(numCourses):
			if dfs(c) == False:
				return []
		return output