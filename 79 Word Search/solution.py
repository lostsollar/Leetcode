# -*- coding: utf-8 -*-


class Solution(object):
    def _exist(self, board, i, j, height, width, word, visited):
        if not len(word):
            return True
        if i < 0 or i >= height or j < 0 or j >= width or board[i][j] != word[0] or visited[i][j]:
            return False
        visited[i][j] = True
        res = self._exist(board, i - 1, j, height, width, word[1:], visited)
        if not res:
            res = self._exist(board, i + 1, j, height, width, word[1:], visited)
        if not res:
            res = self._exist(board, i, j - 1, height, width, word[1:], visited)
        if not res:
            res = self._exist(board, i, j + 1, height, width, word[1:], visited)
        # 如果该结点无法匹配结果，需要将已访问的状态改回未访问
        visited[i][j] = False
        return res

    def exist(self, board, word):
        """
        My own solution
        需要增加一个二维数组记录已访问过的节点
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 无需判断二维数组为空的状态，这里没有这种 case
        height = len(board)
        width = len(board[0])
        visited = [[False] * width for i in range(height)]
        for i in range(height):
            for j in range(width):
                if self._exist(board, i, j, height, width, word, visited):
                    return True
        return False


board1 = [
  ['A', 'B', 'C', 'E'],
  ['S', 'F', 'C', 'S'],
  ['A', 'D', 'E', 'E']
]
board2 = [
    ["a", "a", "a", "a"],
    ["a", "a", "a", "a"],
    ["a", "a", "a", "a"]
]
board3 = [
    ["C", "A", "A"],
    ["A", "A", "A"],
    ["B", "C", "D"]
]
word0 = "aaaaaaaaaaaaa"
word1 = "ABCCED"
word2 = "SEE"
word3 = "ABCB"
word4 = "AAB"
checker = Solution()
print checker.exist(board1, word1)
print checker.exist(board1, word2)
print checker.exist(board1, word3)
print checker.exist(board2, word0)
print checker.exist(board3, word4)




