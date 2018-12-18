# -*- coding=utf-8 -*-


def maxProduct1(nums):
    if nums is None:
        return 0
    res, cur_max, cur_min = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        cur_max, cur_min = cur_max * num, cur_min * num
        cur_max, cur_min = max(cur_max, cur_min, num), min(cur_max, cur_min, num)
        res = cur_max if cur_max > res else res
    return res


def maxProduct2(nums):
    """
    这里使用了「滚动数组」，与上面的区别是增加了维度
    使用了二维数组使表达能力更强，可以适用于更多场景
    这里的dp[0], dp[1]分别交替存上一次的max、min与这次的max、min
    而方法一里直接选择了同时赋值
    :param nums:
    :return:
    """
    if nums is None:
        return 0
    dp = [[0 for _ in range(2)] for _ in range(2)]
    dp[0][0], dp[0][1], res = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        x, y = i % 2, (i - 1) % 2
        dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
        dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
        res = max(res, dp[x][0])
    return res


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
    test1 = [2, 3, -2, 4]
    test2 = [-2, 0, -1]
    test3 = [2, 3, -4, 1, -2, 4]
    test4 = [3, -1, 4]
    test5 = [2, -5, -2, -4, 3]
    test6 = [2, 3, -4, -2, 4]
    tests = [test1, test2, test3, test4, test5, test6]

    check_result(maxProduct1, tests)
    check_result(maxProduct2, tests)
