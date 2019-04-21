# -*- coding: utf-8 -*-


# 并查集
class UnionFind(object):
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m*n)
        self.rank = [0] * (m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i*n + j] = i*n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1


class Solution(object):
    def __init__(self):
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]

    def floodFill(self, grid, i, j):
        if i < 0 or i >= self.height or j < 0 or j >= self.width or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.floodFill(grid, i - 1, j)
        self.floodFill(grid, i + 1, j)
        self.floodFill(grid, i, j - 1)
        self.floodFill(grid, i, j + 1)

    def numIslands0(self, grid):
        """
        My own solution，染色问题[Flood Fill, DFS]
        Reference: https://leetcode.com/problems/number-of-islands/submissions/
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        self.height = len(grid)
        self.width = len(grid[0])
        counter = 0
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == "1":
                    counter += 1
                    self.floodFill(grid, i, j)
        return counter

    def _is_valid(self, x, y):
        if x < 0 or x >= self.height or y < 0 or y >= self.width:
            return False
        if self.grid[x][y] == '0' or ((x, y) in self.visited):
            return False
        return True

    def floodFill_DFS(self, x, y):
        if not self._is_valid(x, y):
            return 0
        self.visited.add((x, y))
        for k in range(4):
            self.floodFill_DFS(x + self.dx[k], y + self.dy[k])
        return 1

    def numIslands1(self, grid):
        """
        染色问题[Flood Fill, DFS]
        https://leetcode.com/problems/number-of-islands/submissions/
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        self.height = len(grid)
        self.width = len(grid[0])
        self.grid = grid
        self.visited = set()
        return sum([self.floodFill_DFS(i, j) for i in range(self.height) for j in range(self.width)])

    def numIslands2(self, grid):
        if not grid or not grid[0]:
            return 0
        uf = UnionFind(grid)
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                for d in directions:
                    nr, nc = i + d[0], j + d[1]
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                        uf.union(i*n+j, nr*n+nc)
        return uf.count

    def numIslands(self, grid):
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == "1":
                grid[i][j] = '0'
                map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))


test1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

test2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

checker = Solution()
print checker.numIslands(test2)