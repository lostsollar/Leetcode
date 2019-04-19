# coding=utf-8
# -*- coding: utf-8 -*-


class Solution(object):
    def minDistance(self, word1, word2):
        """
        DP
        https://time.geekbang.org/course/detail/130-69785
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        # 如果 word2 为0，那么 word1 变为 word2 需要删除 i 次
        for i in range(m+1):
            dp[i][0] = i
        # 如果 word1 为0，那么 word1 变为 word2 需要增加 j 次
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = min(
                    dp[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1),
                    dp[i-1][j] + 1,
                    dp[i][j-1] + 1
                )
        return dp[m][n]