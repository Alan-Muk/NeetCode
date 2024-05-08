## given a 2D grid where 1's represent land, 0's represent water, count the nuumber of islands

class Solution:
	def numIslands(self, grid:list[list[int]]) -> int:
		if not grid:
			return 0

		rows, cols = len(grid), len(grid[0])
		visit = set()
		islands = 0

		def bfs(r,c):
			q = collections.deque()
			visit.add((r,c))
			q.append((r,c))

			while q:
				row, col = q.popleft()
				directions = [[1,0], [-1,0], [0,1], [0, -1]]

				for dr, dc in directions:
					if((r + dr) in range(rows) and
						(c + dc) in range(cols) and
						grid[r + dr][c + dc] == "1" and
						(r + dr, c + dc) not in visit):
						q.append((r + dr, c + dc))
						visit.add((r + dr, c + dc))

		for r in range(rows):
			for c in range(cols):
				if grid[r][c] == "1" and (r,c) not in visit:
					bfs(r,c)
					islands += 1

		return islands