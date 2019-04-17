# -*- coding: utf-8 -*-


class Solution(object):
    def countBits0(self, num):
        """
        My own solution
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1) if num > 0 else [0]
        n = 1
        while n <= num:
            res[n] = 1
            n <<= 1
        for i in range(3, num + 1):
            if res[i]:
                continue
            # 奇数中1的个数等于比他小的那个偶数中1的个数加1
            if i % 2:
                res[i] = res[i-1] + 1
            # 偶数相当于该偶数除以2之后的结果左移1位，不改变1的个数
            else:
                res[i] = res[i/2]
        return res

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1) if num > 0 else [0]
        for i in range(1, num+1):
            res[i] = res[i & (i-1)] + 1
        return res


checker = Solution()
print checker.countBits(9)

