# -*- coding: utf-8 -*-


class Solution(object):
    def __init__(self):
        self.trie = {}
        self.END_OF_WORD = "#"
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.result = set()

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

    def exist(self, board, height, width, word):
        visited = [[False] * width for i in range(height)]
        for i in range(height):
            for j in range(width):
                if self._exist(board, i, j, height, width, word, visited):
                    return True
        return False

    def findWords0(self, board, words):
        """
        My own Solution: DFS
        Time Limit Exceeded
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        height = len(board)
        width = len(board[0])
        for word in words:
            if self.exist(board, height, width, word):
                res.append(word)
        return res

    def createTrie(self, board, i, j, height, width, visited, trie):
        if i < 0 or i >= height or j < 0 or j >= width:
            return
        if visited[i][j]:
            return
        visited[i][j] = True
        cur = trie.setdefault(board[i][j], {})
        self.createTrie(board, i - 1, j, height, width, visited, cur)
        self.createTrie(board, i + 1, j, height, width, visited, cur)
        self.createTrie(board, i, j - 1, height, width, visited, cur)
        self.createTrie(board, i, j + 1, height, width, visited, cur)
        visited[i][j] = False

    def findWords1(self, board, words):
        """
        My own Solution: 以 board 来构建字典树，时间复杂度较高
        Time Limit Exceeded
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        height = len(board)
        width = len(board[0])
        for i in range(height):
            for j in range(width):
                visited = [[False] * width for x in range(height)]
                self.createTrie(board, i, j, height, width, visited, self.trie)
        res = []
        for word in words:
            flag = True
            node = self.trie
            for char in word:
                if char not in node:
                    flag = False
                    break
                node = node[char]
            if flag:
                res.append(word)
        return res

    def _dfs(self, board, i, j, cur_word, cur_dict):
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]

        if self.END_OF_WORD in cur_dict:
            self.result.add(cur_word)

        # 不用再开一个访问的数组
        tmp, board[i][j] = board[i][j], "@"
        for k in range(4):
            x, y = i + self.dx[k], j + self.dy[k]
            if 0 <= x < self.m and 0 <= y < self.n \
                and board[x][y] != "@" and board[x][y] in cur_dict:
                self._dfs(board, x, y, cur_word, cur_dict)
        board[i][j] = tmp

    def findWords(self, board, words):
        """
        https://time.geekbang.org/course/detail/130-67643
        以 words 构建字典树 Trie
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        if not words:
            return []

        root = {}
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node[self.END_OF_WORD] = self.END_OF_WORD

        self.m, self.n = len(board), len(board[0])

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self._dfs(board, i, j, "", root)

        return list(self.result)


board = [
  ['o', 'a', 'a', 'n'],
  ['e', 't', 'a', 'e'],
  ['i', 'h', 'k', 'r'],
  ['i', 'f', 'l', 'v']
]
board1 = [
    ["a", "b"],
    ["c", "a"]
]
board2 = [
    ["b", "b", "a", "a", "b", "a"],
    ["b", "b", "a", "b", "a", "a"],
    ["b", "b", "b", "b", "b", "b"],
    ["a", "a", "a", "b", "a", "a"],
    ["a", "b", "a", "a", "b", "b"]
]
words = ["oath", "pea", "eat", "rain"]
words1 = ["abbbababaa"]
checker = Solution()
print checker.findWords(board, words)
