# -*- coding=utf-8 -*-

def coinChange(coins, amount):
    """
    Solution: DP [Accepted]
    类似于 Fibonacci, 面值相当于要上的台阶步数
    dp 数组中初值设为比 amount 大1是为了当 dp[amount] 无解时好判断
    Time Complexity: O(amount*len(coins))
    Space Complexity: O(amount)
    :param coins:
    :param amount:
    :return:
    """
    max_value = amount + 1
    dp = [max_value] * max_value
    dp[0] = 0
    for i in range(1, max_value):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin]+1)
    return -1 if dp[max_value-1] > amount else dp[max_value-1]


test1 = [5, 3]
amount1 = 3

test2 = [1, 2, 3]
amount2 = 3

test3 = [1, 2, 5]
amount3 = 11

print coinChange(test2, amount2)