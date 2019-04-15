class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.list = []
        self._gen(0, 0, n, "")
        return self.list

    def _gen(self, left, right, n, result):
        if left == n and right == n:
            self.list.append(result)
        if left < n:
            self._gen(left+1, right, n, result + "(")
        if left > right < n:
            self._gen(left, right+1, n, result + ")")

    def generateParenthesis1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.list = []
        self._gen1(n, n, "")
        return self.list

    def _gen1(self, left, right, result):
        if left == 0 and right == 0:
            self.list.append(result)
        if left > 0:
            self._gen1(left-1, right, result + "(")
        if right > left:
            self._gen1(left, right-1, result + ")")


n = 3
checker = Solution()
print checker.generateParenthesis1(n)