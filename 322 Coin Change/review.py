# coding=utf-8
# -*- coding:utf-8 -*-


class Solution(object):
    def coinChange(self, coins, amount):
        """
        DP
        https://time.geekbang.org/course/detail/130-69784
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        max = amount + 1
        DP = [max] * max
        DP[0] = 0
        for i in range(1, max):
            for j in range(len(coins)):
                if i >= coins[j]:
                    DP[i] = min(DP[i], DP[i-coins[j]] + 1)
        # 如果DP[-1] 大于 amount 表示 DP[-1]没有被更新，说明没有合适的面值组合等于 amount
        return -1 if DP[-1] > amount else DP[-1]


coins1 = [1, 2, 5]
amount1 = 11
coins2 = [3]
amount2 = 2
checker = Solution()
print checker.coinChange(coins2, amount2)
