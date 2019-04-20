# -*- coding: utf-8 -*-


class Solution(object):
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