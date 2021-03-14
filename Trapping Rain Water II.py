import heapq

class Solution:
	def trapRainWater(self, heightMap: List[List[int]]) -> int:
		r, c = len(heightMap), len(heightMap[0])
		if r == 0:
			return 0

		hq = []
		visited = set()
		for i in range(r):
			for j in range(c):
				if i == 0 or j == 0 or i == r - 1 or j == c - 1:
					heapq.heappush(hq, (heightMap[i][j], i, j))
					visited.add((i, j))
		water = 0
		while hq:
			currHeight, row, col = heapq.heappop(hq)
			for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
				new_row, new_col = row + move[0], col + move[1]
				if (new_row, new_col) not in visited and 0 <= new_row < r and 0 <= new_col < c:
					newHeight = heightMap[new_row][new_col]
					water += max(0, currHeight - newHeight)
					heapq.heappush(hq, (max(currHeight, newHeight), new_row, new_col))
					visited.add((new_row, new_col))
		return water
