class UnionFind(object):
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    self.parent[i*n+j] = i*n+j
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
    def floodFill(self, grid, i, j):
        if i < 0 or i >= self.height or j < 0 or j >= self.width or grid[i][j] == 0:
            return
        grid[i][j] = 0
        grid[j][i] = 0
        for y in range(self.width):
            if grid[i][y] == 1:
                self.floodFill(grid, i, y)
            if grid[j][y] == 1:
                self.floodFill(grid, j, y)
        for x in range(self.height):
            if grid[x][j] == 1:
                self.floodFill(grid, x, j)
            if grid[x][i] == 1:
                self.floodFill(grid, x, i)

    def findCircleNum0(self, M):
        """
        My own solution: Flood Fill
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        self.height = len(M)
        self.width = len(M[0])
        counter = 0
        for i in range(self.height):
            for j in range(self.width):
                if M[i][j] == 1:
                    counter += 1
                    self.floodFill(M, i, j)
        return counter

    def findCircleNum(self, M):
        """
        My own solution: Union & Find [Time Limit Exceeded]
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        height, width = len(M), len(M[0])
        uf = UnionFind(M)
        for i in range(height):
            for j in range(width):
                if M[i][j]:
                    uf.union(i * width + j, j * width + i)
                    for y in range(width):
                        if M[i][y] and uf.find(i*width+j) != uf.find(i*width+y):
                            uf.union(i * width + j, i * width + y)
                        if M[j][y] and uf.find(j*width+i) != uf.find(j*width+y):
                            uf.union(j * width + i, j * width + y)
                    for x in range(height):
                        if M[x][j] and uf.find(i*width+j) != uf.find(x*width+j):
                            uf.union(i * width + j, x * width + j)
                        if M[x][i] and uf.find(j*width+i) != uf.find(x*width+i):
                            uf.union(j * width + i, x * width + i)
        return uf.count


test = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
test1 = [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1]
]
test2 = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 1, 1]
]
test3 = [
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
    [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
checker = Solution()
print checker.findCircleNum1(test3)