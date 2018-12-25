# coding=utf-8

def lengthOfLIS1(nums):
    """
    Solution1: DP [Accepted]
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    :param nums:
    :return:
    """
    length = len(nums)
    if length < 2:
        return length
    dp = [1] * length
    for i in range(1, length):
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def search(arr, num):
    length = len(arr)
    index = length
    for i in range(0, length):
        if arr[i] > num:
            index = i
            break
        elif arr[i] == num:
            index = -1
            break
    return index


def lengthOfLIS2(nums):
    """
    Solution2: 构造一个升序数组，然后遍历给定数组的每一个元素 key,
               如果升序数组中有与 key 相等的元素，直接比较数据中下一个元素，
               否则找到第一个比 key 大的元素并进行替换，如果升序数组中元素
               都比 key 小，则将 key 插入到升序数组的末尾
    Time Complexity: O(n^2) 如果将查找程序 search 改为二分搜索则为 O(nlogn)
    Space Complexity: O(n)
    :param nums:
    :return:
    """
    res = []
    for i in range(len(nums)):
        length = len(res)
        index = search(res, nums[i])
        if index == -1:
            continue
        if index == length:
            res.append(nums[i])
        else:
            res[index] = nums[i]
    return len(res)


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
    test1 = [10, 9, 2, 5, 3, 7, 101, 18]
    test2 = [4, 10, 4, 3, 8, 9]
    test3 = [2, 2]
    test4 = [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]
    tests = [test1, test2, test3, test4]
    check_result(lengthOfLIS1, tests)
    check_result(lengthOfLIS2, tests)
