# -*- coding=utf-8 -*-


def maxProfit1(prices):
    """
    Solution1: Brute Force [Time Limit Exceeded]
    两次循环暴力枚举，找出顺序上 diff 最大的两个数字之差
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    :param prices:
    :return:
    """
    if prices is None:
        return 0
    res = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            res = max(res, prices[j]-prices[i])
    return res


def maxProfit2(prices):
    """
    Solution2: DP(my own) [Accepted]
    Time Complexity: O(n)
    Space Complexity: O(1)
    :param prices:
    :return:
    """
    length = len(prices)
    if length == 0:
        return 0
    min_value = prices[0]
    dp = 0
    for i in range(1, length):
        if prices[i] < min_value:
            min_value = prices[i]
        dp = max(dp, prices[i]-min_value)
    return dp


def check_result(func, tests, index=None):
    if index:
        print tests[index]
        print func(tests[index])
        print
    else:
        for test in tests:
            print test
            print func(test)
        print


if __name__ == '__main__':
    test1 = [7, 1, 5, 3, 6, 4]
    test2 = [7, 6, 4, 3, 1]
    tests = [test1, test2]
    check_result(maxProfit1, tests)
    check_result(maxProfit2, tests)
