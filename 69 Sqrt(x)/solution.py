# —*- coding:utf-8 -*-


class Solution(object):
    def mySqrt(self, x):
        """
        My solution binary search
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) / 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                if (mid - 1) * (mid - 1) < x:
                    return mid - 1
                right = mid - 1
            else:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                left = mid + 1


    def mySqrt(self, x):
        """
        牛顿迭代法
        https://time.geekbang.org/course/detail/130-67641
        :param x:
        :return:
        """
        r = x
        while r * r > x:
            r = (r+x/r) / 2
        return r


n = 1
checker = Solution()
print checker.mySqrt(n)